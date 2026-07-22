"""Naturalism scoring: compare generated words against real attested phonotactics."""

from __future__ import annotations

from dataclasses import dataclass

from .generate import Word
from .reference_data import ClusterProfile


@dataclass
class NaturalismReport:
    num_words: int
    avg_syllables_per_word: float
    consonant_vowel_ratio: float | None
    onset_clusters_checked: int
    onset_clusters_attested: int
    coda_clusters_checked: int
    coda_clusters_attested: int

    @property
    def onset_legality_rate(self) -> float | None:
        if not self.onset_clusters_checked:
            return None
        return self.onset_clusters_attested / self.onset_clusters_checked

    @property
    def coda_legality_rate(self) -> float | None:
        if not self.coda_clusters_checked:
            return None
        return self.coda_clusters_attested / self.coda_clusters_checked


def analyze(words: list[Word], cluster_profile: ClusterProfile | None) -> NaturalismReport:
    """Score generated words against a real language's attested consonant clusters.

    Only multi-consonant onsets/codas are checked (single consonants are always
    "legal"). onset/coda_legality_rate is the fraction of generated clusters that
    are actually attested in that language's Phonotacticon data -- a rough proxy
    for how naturalistic the generator's clusters are, not a claim of certainty
    (Phonotacticon coverage is a sample of the language's attested wordlist, not
    an exhaustive phonotactic grammar).
    """
    total_consonants = 0
    total_vowels = 0
    onset_checked = onset_ok = 0
    coda_checked = coda_ok = 0

    for word in words:
        for syllable in word.syllables:
            for slot in syllable.pattern:
                if slot == "C":
                    total_consonants += 1
                else:
                    total_vowels += 1

            if cluster_profile is not None:
                if len(syllable.onset) > 1:
                    onset_checked += 1
                    if syllable.onset in cluster_profile.onsets:
                        onset_ok += 1
                if len(syllable.coda) > 1:
                    coda_checked += 1
                    if syllable.coda in cluster_profile.codas:
                        coda_ok += 1

    cv_ratio = (total_consonants / total_vowels) if total_vowels else None
    avg_syllables = sum(len(w.syllables) for w in words) / len(words) if words else 0.0

    return NaturalismReport(
        num_words=len(words),
        avg_syllables_per_word=avg_syllables,
        consonant_vowel_ratio=cv_ratio,
        onset_clusters_checked=onset_checked,
        onset_clusters_attested=onset_ok,
        coda_clusters_checked=coda_checked,
        coda_clusters_attested=coda_ok,
    )
