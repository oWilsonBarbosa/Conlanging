"""Phoneme inventory definitions for the syllable/word generator."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class SyllablePattern:
    """A syllable shape made of 'C' (consonant) and 'V' (vowel) slots, with a relative weight."""

    pattern: str
    weight: float = 1.0


@dataclass
class Inventory:
    name: str
    consonants: list[str]
    vowels: list[str]
    syllable_patterns: list[SyllablePattern]
    word_length_weights: dict[int, float] = field(default_factory=lambda: {1: 3, 2: 5, 3: 2})
    illegal_sequences: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Inventory:
        patterns = [
            SyllablePattern(p["pattern"], float(p.get("weight", 1.0)))
            for p in data["syllable_patterns"]
        ]
        raw_lengths = data.get("word_length_weights") or {"1": 3, "2": 5, "3": 2}
        word_length_weights = {int(k): float(v) for k, v in raw_lengths.items()}
        return cls(
            name=data.get("name", "Unnamed"),
            consonants=list(dict.fromkeys(data["consonants"])),
            vowels=list(dict.fromkeys(data["vowels"])),
            syllable_patterns=patterns,
            word_length_weights=word_length_weights,
            illegal_sequences=list(data.get("illegal_sequences", [])),
        )

    @classmethod
    def load(cls, path: str | Path) -> Inventory:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        inventory = cls.from_dict(data)
        inventory.validate()
        return inventory

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "consonants": self.consonants,
            "vowels": self.vowels,
            "syllable_patterns": [asdict(p) for p in self.syllable_patterns],
            "word_length_weights": {str(k): v for k, v in self.word_length_weights.items()},
            "illegal_sequences": self.illegal_sequences,
        }

    def save(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps(self.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def validate(self) -> None:
        if not self.consonants:
            raise ValueError("Inventory needs at least one consonant.")
        if not self.vowels:
            raise ValueError("Inventory needs at least one vowel.")
        if not self.syllable_patterns:
            raise ValueError("Inventory needs at least one syllable pattern.")
        for p in self.syllable_patterns:
            if not p.pattern or any(ch not in "CV" for ch in p.pattern):
                raise ValueError(f"Syllable pattern {p.pattern!r} must contain only 'C' and 'V'.")
            if p.weight <= 0:
                raise ValueError(f"Syllable pattern {p.pattern!r} needs a positive weight.")
        if not self.word_length_weights:
            raise ValueError("Inventory needs at least one word-length weight.")
        for length, weight in self.word_length_weights.items():
            if length <= 0:
                raise ValueError("Word lengths must be positive integers (number of syllables).")
            if weight <= 0:
                raise ValueError(f"Word-length weight for {length} syllables must be positive.")


TEMPLATE_INVENTORY: dict[str, Any] = {
    "name": "New Conlang",
    "consonants": ["p", "t", "k", "m", "n", "s", "l", "w", "j"],
    "vowels": ["a", "i", "u"],
    "syllable_patterns": [
        {"pattern": "V", "weight": 1},
        {"pattern": "CV", "weight": 6},
        {"pattern": "CVC", "weight": 3},
    ],
    "word_length_weights": {"1": 3, "2": 5, "3": 2},
    "illegal_sequences": [],
}
