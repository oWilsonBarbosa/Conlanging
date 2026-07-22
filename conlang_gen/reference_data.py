"""Loaders for the real-world phonology data bundled in data/, used for naturalism testing.

All reads happen directly against the zip files, so nothing needs to be
extracted to disk. Sources used:

- PHOIBLE (data/dev-master.zip): phoneme inventories for ~2,700 living
  and historical languages, with an explicit consonant/vowel/tone label
  per phoneme. The primary source for real-language inventories.
- BDPROTO (data/bdproto-master.zip): phoneme inventories for ~800
  languages and proto-languages (mostly reconstructed proto-languages).
  A secondary source, kept for reconstructed/proto-language lookups
  PHOIBLE doesn't cover.
- CLTS BIPA (data/clts-2.3.0.zip): canonical IPA symbol lists, used to
  classify a BDPROTO phoneme as a consonant or vowel (BDPROTO has no
  such column of its own).
- Phonotacticon (data/phonotacticon-main.zip): attested onset/coda
  consonant clusters for ~500 languages, keyed by Glottocode.
"""

from __future__ import annotations

import csv
import io
import zipfile
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

BDPROTO_ZIP = DATA_DIR / "bdproto-master.zip"
BDPROTO_CSV_MEMBER = "bdproto-master/bdproto.csv"

CLTS_ZIP = DATA_DIR / "clts-2.3.0.zip"
CLTS_CONSONANTS_MEMBER = "clts-2.3.0/pkg/transcriptionsystems/bipa/consonants.tsv"
CLTS_VOWELS_MEMBER = "clts-2.3.0/pkg/transcriptionsystems/bipa/vowels.tsv"

PHOIBLE_ZIP = DATA_DIR / "dev-master.zip"
PHOIBLE_CSV_MEMBER = "dev-master/data/phoible.csv"

PHONOTACTICON_ZIP = DATA_DIR / "phonotacticon-main.zip"
PHONOTACTICON_LANGUAGES_MEMBER = "phonotacticon-main/cldf/languages.csv"
PHONOTACTICON_SEQUENCES_MEMBER = "phonotacticon-main/cldf/sequences.csv"


class ReferenceDataError(RuntimeError):
    pass


def _read_csv_member(zip_path: Path, member: str, delimiter: str = ",") -> list[dict[str, str]]:
    if not zip_path.exists():
        raise ReferenceDataError(
            f"Missing reference data file: {zip_path}. It should be checked into data/."
        )
    with zipfile.ZipFile(zip_path) as zf:
        with zf.open(member) as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8")
            return list(csv.DictReader(text, delimiter=delimiter))


@lru_cache(maxsize=1)
def _clts_symbol_sets() -> tuple[frozenset[str], frozenset[str]]:
    consonants = _read_csv_member(CLTS_ZIP, CLTS_CONSONANTS_MEMBER, delimiter="\t")
    vowels = _read_csv_member(CLTS_ZIP, CLTS_VOWELS_MEMBER, delimiter="\t")
    c_set = frozenset(row["GRAPHEME"] for row in consonants if row.get("GRAPHEME"))
    v_set = frozenset(row["GRAPHEME"] for row in vowels if row.get("GRAPHEME"))
    return c_set, v_set


def classify_phoneme(symbol: str) -> str | None:
    """Classify an IPA symbol as 'C', 'V', or None (unrecognized) using CLTS BIPA data."""
    consonants, vowels = _clts_symbol_sets()
    if symbol in vowels:
        return "V"
    if symbol in consonants:
        return "C"
    stripped = symbol.rstrip("ːˑ")  # retry once with trailing length marks removed
    if stripped != symbol:
        if stripped in vowels:
            return "V"
        if stripped in consonants:
            return "C"
    return None


@lru_cache(maxsize=1)
def _bdproto_rows() -> list[dict[str, str]]:
    return _read_csv_member(BDPROTO_ZIP, BDPROTO_CSV_MEMBER)


def search_bdproto_languages(query: str, limit: int = 25) -> list[str]:
    query = query.lower().strip()
    names = {
        row["LanguageName"]
        for row in _bdproto_rows()
        if row.get("LanguageName") and row["LanguageName"] != "NA"
    }
    matches = sorted(name for name in names if query in name.lower())
    return matches[:limit]


@dataclass
class RealInventory:
    language_name: str
    glottocode: str | None
    consonants: list[str]
    vowels: list[str]
    unclassified: list[str]
    source: str = "bdproto"
    inventory_id: str | None = None
    other_inventory_ids: tuple[str, ...] = ()


def load_bdproto_inventory(language_name: str) -> RealInventory:
    rows = [
        row for row in _bdproto_rows() if row.get("LanguageName", "").lower() == language_name.lower()
    ]
    if not rows:
        raise ReferenceDataError(
            f"No BDPROTO language matches {language_name!r} exactly. "
            "Use search_bdproto_languages() to find valid names."
        )
    phonemes = list(
        dict.fromkeys(row["Phoneme"] for row in rows if row.get("Phoneme") and row["Phoneme"] != "NA")
    )
    glottocode = rows[0].get("Glottocode") or None
    if glottocode == "NA":
        glottocode = None

    consonants: list[str] = []
    vowels: list[str] = []
    unclassified: list[str] = []
    for phoneme in phonemes:
        kind = classify_phoneme(phoneme)
        if kind == "C":
            consonants.append(phoneme)
        elif kind == "V":
            vowels.append(phoneme)
        else:
            unclassified.append(phoneme)

    return RealInventory(
        language_name=rows[0]["LanguageName"],
        glottocode=glottocode,
        consonants=consonants,
        vowels=vowels,
        unclassified=unclassified,
    )


@lru_cache(maxsize=1)
def _phoible_rows() -> list[dict[str, str]]:
    return _read_csv_member(PHOIBLE_ZIP, PHOIBLE_CSV_MEMBER)


def search_phoible_languages(query: str, limit: int = 25) -> list[str]:
    query = query.lower().strip()
    names = {row["LanguageName"] for row in _phoible_rows() if row.get("LanguageName")}
    matches = sorted(name for name in names if query in name.lower())
    return matches[:limit]


def list_phoible_inventory_ids(language_name: str) -> list[str]:
    """Distinct PHOIBLE source inventories available for a language name (it can have more
    than one, since PHOIBLE aggregates independent phonological descriptions)."""
    ids = {
        row["InventoryID"]
        for row in _phoible_rows()
        if row.get("LanguageName", "").lower() == language_name.lower()
    }
    return sorted(ids, key=int)


def load_phoible_inventory(language_name: str, inventory_id: str | None = None) -> RealInventory:
    candidates = [
        row for row in _phoible_rows() if row.get("LanguageName", "").lower() == language_name.lower()
    ]
    if not candidates:
        raise ReferenceDataError(
            f"No PHOIBLE language matches {language_name!r} exactly. "
            "Use search_phoible_languages() to find valid names."
        )

    available_ids = sorted({row["InventoryID"] for row in candidates}, key=int)
    if inventory_id is None:
        if len(available_ids) == 1:
            inventory_id = available_ids[0]
        else:
            # Default to whichever source inventory lists the most phonemes.
            counts = {
                inv_id: sum(1 for row in candidates if row["InventoryID"] == inv_id)
                for inv_id in available_ids
            }
            inventory_id = max(available_ids, key=lambda inv_id: counts[inv_id])
    elif inventory_id not in available_ids:
        raise ReferenceDataError(
            f"PHOIBLE inventory ID {inventory_id!r} not found for {language_name!r}. "
            f"Available IDs: {', '.join(available_ids)}."
        )

    rows = [row for row in candidates if row["InventoryID"] == inventory_id]
    consonants: list[str] = []
    vowels: list[str] = []
    seen: set[str] = set()
    for row in rows:
        if row.get("Marginal") == "TRUE":
            continue  # peripheral/loanword-only phoneme
        phoneme = row["Phoneme"]
        if phoneme in seen:
            continue
        seen.add(phoneme)
        if row["SegmentClass"] == "consonant":
            consonants.append(phoneme)
        elif row["SegmentClass"] == "vowel":
            vowels.append(phoneme)
        # "tone" segments are suprasegmental, not slotted into C/V syllable patterns.

    glottocode = rows[0].get("Glottocode") or None
    if glottocode == "NA":
        glottocode = None

    return RealInventory(
        language_name=rows[0]["LanguageName"],
        glottocode=glottocode,
        consonants=consonants,
        vowels=vowels,
        unclassified=[],
        source="phoible",
        inventory_id=inventory_id,
        other_inventory_ids=tuple(i for i in available_ids if i != inventory_id),
    )


@lru_cache(maxsize=1)
def _phonotacticon_languages() -> list[dict[str, str]]:
    return _read_csv_member(PHONOTACTICON_ZIP, PHONOTACTICON_LANGUAGES_MEMBER)


@lru_cache(maxsize=1)
def _phonotacticon_sequences() -> list[dict[str, str]]:
    return _read_csv_member(PHONOTACTICON_ZIP, PHONOTACTICON_SEQUENCES_MEMBER)


def find_phonotacticon_language_id(glottocode: str) -> str | None:
    for row in _phonotacticon_languages():
        if row.get("Glottocode") == glottocode:
            return row["ID"]
    return None


@dataclass
class ClusterProfile:
    language_id: str
    onsets: set[tuple[str, ...]]
    codas: set[tuple[str, ...]]

    @property
    def max_onset_length(self) -> int:
        return max((len(o) for o in self.onsets), default=0)

    @property
    def max_coda_length(self) -> int:
        return max((len(c) for c in self.codas), default=0)


def load_cluster_profile(language_id: str) -> ClusterProfile:
    groups: dict[str, dict[str, list[tuple[int, str]]]] = {"Onset": {}, "Coda": {}}
    for row in _phonotacticon_sequences():
        if row.get("Language_ID") != language_id:
            continue
        category = row.get("Category")
        if category not in groups:
            continue
        groups[category].setdefault(row["Sequence"], []).append((int(row["Order"]), row["Segment"]))

    def _finalize(sequences: dict[str, list[tuple[int, str]]]) -> set[tuple[str, ...]]:
        result = set()
        for segs in sequences.values():
            segs.sort()
            result.add(tuple(seg for _, seg in segs))
        return result

    return ClusterProfile(
        language_id=language_id,
        onsets=_finalize(groups["Onset"]),
        codas=_finalize(groups["Coda"]),
    )
