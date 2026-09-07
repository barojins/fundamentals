"""
LeetCode 304: Range Sum Query 2D - Immutable
Difficulty: Medium
Tags: Array, Design, Matrix, Prefix Sum

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Immutable 2D range sum query inside a rectangle.

Implement `NumMatrix`:
- `int sumRegion(int row1, int col1, int row2, int col2)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
sumRegion(2, 1, 4, 3) -> 8

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `sumRegion`: O(1)
Space Complexity: O(R * C)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
2D prefix sum grid.
"""

import unittest


class NumMatrix:
    """2D immutable range sum query using 2D prefix sum table."""

    def __init__(self, matrix: list[list[int]]) -> None:
        if not matrix or not matrix[0]:
            self.dp: list[list[int]] = [[]]
            return
        R, C = len(matrix), len(matrix[0])
        self.dp = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                self.dp[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.dp[r][c + 1]
                    + self.dp[r + 1][c]
                    - self.dp[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )


class TestNumMatrix(unittest.TestCase):
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
        self.assertEqual(nm.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(nm.sumRegion(1, 2, 2, 4), 12)


if __name__ == "__main__":
    unittest.main()
