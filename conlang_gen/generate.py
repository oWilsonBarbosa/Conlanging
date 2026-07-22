"""Core syllable and word generation engine."""

from __future__ import annotations

import random
from dataclasses import dataclass

from .inventory import Inventory

DEFAULT_MAX_RETRIES = 50


@dataclass
class Syllable:
    pattern: str
    phonemes: list[str]

    @property
    def text(self) -> str:
        return "".join(self.phonemes)

    @property
    def onset(self) -> tuple[str, ...]:
        """Leading consonant run of the syllable, e.g. ('s', 't') for 'stra'."""
        onset: list[str] = []
        for slot, phoneme in zip(self.pattern, self.phonemes):
            if slot != "C":
                break
            onset.append(phoneme)
        return tuple(onset)

    @property
    def coda(self) -> tuple[str, ...]:
        """Trailing consonant run of the syllable, e.g. ('n', 't') for 'ant'."""
        coda: list[str] = []
        for slot, phoneme in zip(reversed(self.pattern), reversed(self.phonemes)):
            if slot != "C":
                break
            coda.append(phoneme)
        return tuple(reversed(coda))


@dataclass
class Word:
    syllables: list[Syllable]

    @property
    def text(self) -> str:
        return "".join(s.text for s in self.syllables)


def _weighted_choice(rng: random.Random, items: list, weights: list[float]):
    return rng.choices(items, weights=weights, k=1)[0]


def generate_syllable(inventory: Inventory, rng: random.Random) -> Syllable:
    pattern = _weighted_choice(
        rng, inventory.syllable_patterns, [p.weight for p in inventory.syllable_patterns]
    ).pattern
    phonemes = [
        rng.choice(inventory.consonants) if slot == "C" else rng.choice(inventory.vowels)
        for slot in pattern
    ]
    return Syllable(pattern=pattern, phonemes=phonemes)


def _has_illegal_sequence(text: str, illegal_sequences: list[str]) -> bool:
    return any(seq in text for seq in illegal_sequences)


def generate_word(
    inventory: Inventory,
    rng: random.Random,
    max_retries: int = DEFAULT_MAX_RETRIES,
) -> Word:
    lengths = list(inventory.word_length_weights.keys())
    weights = list(inventory.word_length_weights.values())
    num_syllables = _weighted_choice(rng, lengths, weights)

    word = Word(syllables=[])
    for _ in range(max_retries):
        syllables = [generate_syllable(inventory, rng) for _ in range(num_syllables)]
        text = "".join(s.text for s in syllables)
        if not _has_illegal_sequence(text, inventory.illegal_sequences):
            return Word(syllables=syllables)
        word = Word(syllables=syllables)
    return word  # best effort after exhausting retries


def generate_words(
    inventory: Inventory,
    count: int,
    rng: random.Random | None = None,
    unique: bool = True,
) -> list[Word]:
    rng = rng or random.Random()
    words: list[Word] = []
    seen: set[str] = set()
    max_attempts = count * 50 + 100
    attempts = 0
    while len(words) < count and attempts < max_attempts:
        attempts += 1
        word = generate_word(inventory, rng)
        if unique:
            if word.text in seen:
                continue
            seen.add(word.text)
        words.append(word)
    return words
