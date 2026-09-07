"""
LeetCode 251: Flatten 2D Vector
Difficulty: Medium
Tags: Array, Two Pointers, Design, Iterator

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an iterator to flatten a 2D vector.

Implement the `Vector2D` class:
- `Vector2D(int[][] vec)`
- `next()` returns the next element.
- `hasNext()` returns `true` if elements remain.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
Output:
[null, 1, 2, 3, true, true, 4, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next`, `hasNext`: O(1) amortized
Space Complexity: O(1) extra space.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain `row` and `col` pointers, lazily advancing past empty rows.
"""

import unittest


class Vector2D:
    """Iterator to flatten a 2D array with O(1) extra space."""

    def __init__(self, vec: list[list[int]]) -> None:
        self.vec: list[list[int]] = vec
        self.row: int = 0
        self.col: int = 0

    def _advance(self) -> None:
        while self.row < len(self.vec) and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        self._advance()
        val = self.vec[self.row][self.col]
        self.col += 1
        return val

    def hasNext(self) -> bool:
        self._advance()
        return self.row < len(self.vec)


class TestVector2D(unittest.TestCase):
    def test_example_1(self) -> None:
        v = Vector2D([[1, 2], [3], [4]])
        self.assertEqual(v.next(), 1)
        self.assertEqual(v.next(), 2)
        self.assertEqual(v.next(), 3)
        self.assertTrue(v.hasNext())
        self.assertEqual(v.next(), 4)
        self.assertFalse(v.hasNext())

    def test_empty_rows(self) -> None:
        v = Vector2D([[], [1], [], [], [2, 3], []])
        out = []
        while v.hasNext():
            out.append(v.next())
        self.assertEqual(out, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
