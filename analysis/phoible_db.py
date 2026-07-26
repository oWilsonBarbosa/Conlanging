"""Loaders for the typological datasets in ``data/``.

Everything is read straight out of the shipped zip files, so nothing has to be
unpacked first. Parsed PHOIBLE data is cached as a pickle because the CSV is
~24 MB and parsing it takes a few seconds.
"""

import csv
import io
import pickle
import sys
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path

csv.field_size_limit(10 ** 7)

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
CACHE = Path(__file__).resolve().parent / ".cache"

PHOIBLE_ZIP = DATA / "dev-master.zip"
PHOIBLE_CSV = "dev-master/data/phoible.csv"
CLTS_ZIP = DATA / "clts-2.3.0.zip"
CLTS_SOUNDS = "clts-2.3.0/data/sounds.tsv"
PBASE_ZIP = DATA / "pbasefiles.zip"
PBASE_PATTERNS = "pbase/pb_patterns.csv"

CACHE_VERSION = 1


def norm(segment):
    """Normalize a segment to NFD.

    IPA has both precomposed and decomposed forms for anything with a
    diacritic -- 'i' + combining tilde is not equal to precomposed 'ĩ' unless
    both go through the same normalization. Every comparison in this package
    runs through here.
    """
    return unicodedata.normalize("NFD", segment.strip())


class Phoible:
    """Segment inventories from PHOIBLE, deduplicated to one per language.

    PHOIBLE ships 3,020 inventories but only ~2,176 distinct Glottocodes; well
    described languages appear several times. Counting raw inventories would
    weight those languages more heavily, so we keep the first inventory
    encountered per Glottocode. File order is stable, so this is deterministic.
    """

    def __init__(self, inventories, seg_class):
        self.inventories = inventories
        self.seg_class = seg_class
        self.n = len(inventories)
        self.counts = Counter()
        for inv in inventories:
            self.counts.update(inv)
        self._index = {}

    @classmethod
    def load(cls, use_cache=True):
        cache_file = CACHE / f"phoible-v{CACHE_VERSION}.pkl"
        if use_cache and cache_file.exists():
            with cache_file.open("rb") as fh:
                return cls(*pickle.load(fh))

        if not PHOIBLE_ZIP.exists():
            raise SystemExit(
                f"missing {PHOIBLE_ZIP}\n"
                "PHOIBLE is required. It ships in this repo as data/dev-master.zip."
            )

        by_inventory = {}
        meta = {}
        classes = {}
        with zipfile.ZipFile(PHOIBLE_ZIP) as z, z.open(PHOIBLE_CSV) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf8"))
            for row in reader:
                seg = norm(row["Phoneme"])
                by_inventory.setdefault(row["InventoryID"], set()).add(seg)
                meta[row["InventoryID"]] = row["Glottocode"]
                cls_name = row["SegmentClass"]
                if cls_name and cls_name != "NA":
                    classes.setdefault(seg, Counter())[cls_name] += 1

        first_per_language = {}
        for inv_id, glottocode in meta.items():
            if glottocode and glottocode != "NA":
                first_per_language.setdefault(glottocode, inv_id)

        inventories = [by_inventory[i] for i in first_per_language.values()]
        seg_class = {s: c.most_common(1)[0][0] for s, c in classes.items()}

        CACHE.mkdir(exist_ok=True)
        with cache_file.open("wb") as fh:
            pickle.dump((inventories, seg_class), fh)
        return cls(inventories, seg_class)

    def languages_with(self, segment):
        """Indices of languages whose inventory contains ``segment``."""
        segment = norm(segment)
        if segment not in self._index:
            self._index[segment] = {
                i for i, inv in enumerate(self.inventories) if segment in inv
            }
        return self._index[segment]

    def frequency(self, segment):
        """Share of languages having this segment, in [0, 1]."""
        return self.counts.get(norm(segment), 0) / self.n

    def sizes(self):
        return sorted(len(inv) for inv in self.inventories)

    def implications(self, segment, min_conditional=0.90, min_languages=25):
        """Segments that ``segment`` implies.

        Yields (implied, P(B|A), lift, n_source, exceptions). Lift is
        P(B|A) - P(B), and it is reported rather than applied: filtering on it
        here would discard true implications whose target is simply very
        common. /ĩ/ implies /i/ without exception, but /i/ is in 93.6% of
        languages, so the lift is only 6 points. The caller decides what to do
        with that -- see report_implications in inventory_check.py.
        """
        source = self.languages_with(segment)
        if len(source) < min_languages:
            return []

        found = []
        for candidate, count in self.counts.items():
            if candidate == norm(segment):
                continue
            overlap = len(source & self.languages_with(candidate))
            conditional = overlap / len(source)
            if conditional >= min_conditional:
                found.append(
                    (
                        candidate,
                        conditional,
                        conditional - count / self.n,
                        len(source),
                        len(source) - overlap,
                    )
                )
        found.sort(key=lambda r: -r[1])
        return found


def clts_names():
    """Map NFD grapheme -> CLTS sound name, e.g. 'ɖ' -> 'voiced retroflex stop'."""
    if not CLTS_ZIP.exists():
        return {}
    names = {}
    with zipfile.ZipFile(CLTS_ZIP) as z, z.open(CLTS_SOUNDS) as raw:
        reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf8"), delimiter="\t")
        for row in reader:
            grapheme = row.get("GRAPHEME", "")
            name = row.get("NAME", "")
            if grapheme and name and name != "<NA>":
                names.setdefault(norm(grapheme), name)
    return names


def counterpart_distance(name_a, name_b):
    """Feature distance between two CLTS sound names, or None if unknown.

    CLTS names are feature strings: 'voiced alveolar sibilant fricative
    consonant'. Treating them as word sets gives a cheap featural distance --
    /z/ and /s/ differ by {voiced, voiceless} = 2, while /z/ and /b/ differ by
    5. That is enough to tell a markedness counterpart from two segments that
    merely co-occur because they are both common.
    """
    if not name_a or not name_b:
        return None
    words_a, words_b = set(name_a.split()), set(name_b.split())
    # 'consonant' vs 'vowel' -- different sound types are never counterparts.
    if name_a.split()[-1] != name_b.split()[-1]:
        return None
    return len(words_a ^ words_b)


def adds_features(name_a, name_b):
    """True if sound A is sound B with extra features piled on.

    'nasalized unrounded close front vowel' over 'unrounded close front vowel'
    -- A is B plus nasalization. This is the one case where a marked segment
    implies its base no matter how common that base is, because the base is
    what you get by removing something you added. Contrast /p/ and /k/, which
    swap a feature rather than adding one and so are not in this relation.
    """
    if not name_a or not name_b:
        return False
    words_a, words_b = set(name_a.split()), set(name_b.split())
    return words_b < words_a


def pbase_rules(segments):
    """Attested phonological rules targeting any of ``segments``.

    Returns {segment: [(language, output, environment, description), ...]}.
    PBase covers 306 languages, so treat this as a plausibility sampler for
    allophony rather than a frequency estimate.
    """
    wanted = {norm(s) for s in segments}
    out = {s: [] for s in wanted}
    if not PBASE_ZIP.exists():
        return out

    with zipfile.ZipFile(PBASE_ZIP) as z, z.open(PBASE_PATTERNS) as raw:
        stream = io.TextIOWrapper(raw, encoding="utf8", errors="replace")
        for row in csv.DictReader(stream, delimiter="\t"):
            if row.get("type", "").strip() != "Target":
                continue
            source = norm(row.get("I", ""))
            if source not in wanted:
                continue
            left = row.get("L1", "").strip()
            right = row.get("R1", "").strip()
            # Most PBase rows leave L1/R1 empty and state the environment in
            # the prose description instead.
            environment = f"{left or ''}__{right or ''}" if (left or right) else ""
            out[source].append(
                (
                    row.get("language", "").strip(),
                    row.get("O", "").strip(),
                    environment,
                    row.get("description_OLD", "").strip(),
                )
            )

    # One language often contributes the same rule several times (once per
    # morphological trigger). Collapse those so a short sample stays varied.
    for segment, rules in out.items():
        seen = set()
        deduped = []
        for rule in rules:
            key = (rule[1], rule[3])
            if key not in seen:
                seen.add(key)
                deduped.append(rule)
        out[segment] = deduped
    return out


def read_inventory(path):
    """Parse an inventory file: one segment per line, or space/comma separated.

    '#' starts a comment. Blank lines are ignored.
    """
    text = Path(path).read_text(encoding="utf8")
    segments = []
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        for chunk in line.replace(",", " ").split():
            segments.append(norm(chunk))

    seen = set()
    unique = []
    for s in segments:
        if s not in seen:
            seen.add(s)
            unique.append(s)
    if len(unique) != len(segments):
        print(
            f"note: dropped {len(segments) - len(unique)} duplicate segment(s)",
            file=sys.stderr,
        )
    return unique
