"""Build a generator Inventory from a real BDPROTO language, and score naturalism."""

from __future__ import annotations

from dataclasses import dataclass

from .inventory import Inventory, SyllablePattern
from .reference_data import (
    ClusterProfile,
    RealInventory,
    find_phonotacticon_language_id,
    load_bdproto_inventory,
    load_cluster_profile,
)


def _default_patterns(cluster_profile: ClusterProfile | None) -> list[SyllablePattern]:
    """Universal-ish syllable shapes, biased toward cluster complexity actually attested
    for this language in Phonotacticon, when a match is available."""
    patterns = [
        SyllablePattern("V", 2),
        SyllablePattern("CV", 6),
        SyllablePattern("CVC", 3),
    ]
    if cluster_profile is not None:
        if cluster_profile.max_onset_length >= 2:
            patterns.append(SyllablePattern("CCV", 1.5))
            patterns.append(SyllablePattern("CCVC", 1))
        if cluster_profile.max_coda_length >= 2:
            patterns.append(SyllablePattern("CVCC", 1))
    return patterns


@dataclass
class RealLanguageResult:
    inventory: Inventory
    real_inventory: RealInventory
    cluster_profile: ClusterProfile | None


def build_inventory_from_language(language_name: str) -> RealLanguageResult:
    """Load a real phoneme inventory from BDPROTO and turn it into a usable Inventory.

    If the language can be matched to Phonotacticon via Glottocode, the returned
    cluster_profile can be used by conlang_gen.stats to score generated words
    against clusters actually attested in that language.
    """
    real = load_bdproto_inventory(language_name)
    if not real.consonants:
        raise ValueError(
            f"{real.language_name!r} has no phonemes classifiable as consonants; "
            "cannot build a syllable generator from it."
        )
    if not real.vowels:
        raise ValueError(
            f"{real.language_name!r} has no phonemes classifiable as vowels; "
            "cannot build a syllable generator from it."
        )

    cluster_profile = None
    if real.glottocode:
        lang_id = find_phonotacticon_language_id(real.glottocode)
        if lang_id:
            cluster_profile = load_cluster_profile(lang_id)

    inventory = Inventory(
        name=real.language_name,
        consonants=real.consonants,
        vowels=real.vowels,
        syllable_patterns=_default_patterns(cluster_profile),
    )
    inventory.validate()
    return RealLanguageResult(inventory=inventory, real_inventory=real, cluster_profile=cluster_profile)
