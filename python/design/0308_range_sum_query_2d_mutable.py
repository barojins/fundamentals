"""
LeetCode 308: Range Sum Query 2D - Mutable
Difficulty: Hard
Tags: Array, Design, Binary Indexed Tree, Segment Tree, Matrix

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Mutable 2D range sum query.

Implement `NumMatrix`:
- `void update(int row, int col, int val)`
- `int sumRegion(int row1, int col1, int row2, int col2)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
sumRegion(2, 1, 4, 3) -> 8, update(3, 2, 2), sumRegion(2, 1, 4, 3) -> 10

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `update`, `sumRegion`: O(log R * log C)
Space Complexity: O(R * C)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
2D Binary Indexed Tree.
"""

import unittest


class NumMatrix:
    """2D mutable range sum queries using a 2D Binary Indexed Tree (Fenwick Tree)."""

    def __init__(self, matrix: list[list[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        self.R: int = len(matrix)
        self.C: int = len(matrix[0])
        self.matrix: list[list[int]] = [row[:] for row in matrix]
        self.tree: list[list[int]] = [[0] * (self.C + 1) for _ in range(self.R + 1)]

        for r in range(self.R):
            for c in range(self.C):
                self._add(r + 1, c + 1, matrix[r][c])

    def _add(self, r: int, c: int, delta: int) -> None:
        i = r
        while i <= self.R:
            j = c
            while j <= self.C:
                self.tree[i][j] += delta
                j += j & -j
            i += i & -i

    def _query(self, r: int, c: int) -> int:
        total = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                total += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return total

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._add(row + 1, col + 1, delta)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self._query(row2 + 1, col2 + 1)
            - self._query(row1, col2 + 1)
            - self._query(row2 + 1, col1)
            + self._query(row1, col1)
        )


class TestNumMatrixMutable(unittest.TestCase):
    def test_example_1(self) -> None:
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
        nm = NumMatrix(matrix)
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 8)
        nm.update(3, 2, 2)
        self.assertEqual(nm.sumRegion(2, 1, 4, 3), 10)


if __name__ == "__main__":
    unittest.main()
