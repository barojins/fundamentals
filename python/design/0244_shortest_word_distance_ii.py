"""
LeetCode 244: Shortest Word Distance II
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, String, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that answers shortest word distance queries for words in an array.

Implement the `WordDistance` class:
- `WordDistance(String[] wordsDict)`
- `int shortest(String word1, String word2)` Returns shortest distance between words.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output:
[null, 3, 1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N)
- `shortest`: O(K1 + K2) two-pointer merge scan on index lists.
Space Complexity: O(N) for indices map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map word -> sorted list of indices. Use two pointers to find minimum index difference.
"""

import unittest
from collections import defaultdict


class WordDistance:
    """Finds the shortest distance between two words in a dictionary using precomputed index lists."""

    def __init__(self, wordsDict: list[str]) -> None:
        self.locations: dict[str, list[int]] = defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.locations[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        locs1 = self.locations[word1]
        locs2 = self.locations[word2]
        p1, p2 = 0, 0
        min_dist = float("inf")

        while p1 < len(locs1) and p2 < len(locs2):
            i1, i2 = locs1[p1], locs2[p2]
            min_dist = min(min_dist, abs(i1 - i2))
            if i1 < i2:
                p1 += 1
            else:
                p2 += 1

        return int(min_dist)


class TestWordDistance(unittest.TestCase):
    def test_example_1(self) -> None:
        wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
        self.assertEqual(wd.shortest("coding", "practice"), 3)
        self.assertEqual(wd.shortest("makes", "coding"), 1)

    def test_multiple_occurrences(self) -> None:
        wd = WordDistance(["a", "c", "b", "a", "b"])
        self.assertEqual(wd.shortest("a", "b"), 1)


if __name__ == "__main__":
    unittest.main()
