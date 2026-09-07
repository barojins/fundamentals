"""
LeetCode 288: Unique Word Abbreviation
Difficulty: Medium
Tags: Array, Hash Table, String, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Determine if a word's abbreviation is unique against a dictionary.

Implement `ValidWordAbbr`:
- `ValidWordAbbr(String[] dictionary)`
- `boolean isUnique(String word)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
Output:
[null, false, true, false, true, true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N * L)
- `isUnique`: O(L)
Space Complexity: O(N * L)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map abbreviation -> set of words. Unique if abbr not in map or maps only to word itself.
"""

import unittest
from collections import defaultdict


class ValidWordAbbr:
    """Validates if a word's abbreviation is unique against a dictionary."""

    def __init__(self, dictionary: list[str]) -> None:
        self.abbr_to_words: dict[str, set[str]] = defaultdict(set)
        for word in dictionary:
            abbr = self._get_abbr(word)
            self.abbr_to_words[abbr].add(word)

    def _get_abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return f"{word[0]}{len(word) - 2}{word[-1]}"

    def isUnique(self, word: str) -> bool:
        abbr = self._get_abbr(word)
        words = self.abbr_to_words[abbr]
        return len(words) == 0 or (len(words) == 1 and word in words)


class TestValidWordAbbr(unittest.TestCase):
    def test_example_1(self) -> None:
        vwa = ValidWordAbbr(["deer", "door", "cake", "card"])
        self.assertFalse(vwa.isUnique("dear"))
        self.assertTrue(vwa.isUnique("cart"))
        self.assertFalse(vwa.isUnique("cane"))
        self.assertTrue(vwa.isUnique("make"))
        self.assertTrue(vwa.isUnique("cake"))


if __name__ == "__main__":
    unittest.main()
