"""
LeetCode 1286: Iterator for Combination
Difficulty: Medium
Tags: String, Backtracking, Design, Iterator

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design the `CombinationIterator` class:
- `CombinationIterator(string characters, int combinationLength)` Initializes the object with a string `characters` of sorted distinct lowercase English letters and a number `combinationLength` as arguments.
- `next()` Returns the next combination of length `combinationLength` in lexicographical order.
- `hasNext()` Returns `true` if and only if there exists a next combination.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output:
[null, "ab", true, "ac", true, "bc", false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next()`, `hasNext()`: O(1) amortized
Space Complexity: O(C(N, K) * K) precomputed or O(K) index generator.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Precompute or generate lazily all combinations using backtracking / `itertools.combinations`.
Store in a list `self.combos` with cursor pointer `self.idx`.
"""

import unittest
from itertools import combinations


class CombinationIterator:
    """Lexicographical combination iterator."""

    def __init__(self, characters: str, combinationLength: int) -> None:
        self.combos: list[str] = [
            "".join(c) for c in combinations(characters, combinationLength)
        ]
        self.idx: int = 0

    def next(self) -> str:
        val = self.combos[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.combos)
class TestCombinationIterator(unittest.TestCase):
    def test_example_1(self) -> None:
        itr = CombinationIterator("abc", 2)
        self.assertEqual(itr.next(), "ab")
        self.assertTrue(itr.hasNext())
        self.assertEqual(itr.next(), "ac")
        self.assertTrue(itr.hasNext())
        self.assertEqual(itr.next(), "bc")
        self.assertFalse(itr.hasNext())


if __name__ == "__main__":
    unittest.main()
