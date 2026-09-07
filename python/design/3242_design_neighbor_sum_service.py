"""
LeetCode 3242: Design Neighbor Sum Service
Difficulty: Easy
Tags: Array, Hash Table, Design, Matrix, Simulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given an `n x n` 2D array `grid` containing distinct elements in the range `[0, n^2 - 1]`.

Implement the `NeighborSum` class:
- `NeighborSum(int[][] grid)`
- `int adjacentSum(int value)` Returns the sum of adjacent (horizontal/vertical) neighbors of `value`.
- `int diagonalSum(int value)` Returns the sum of diagonal (top-left, top-right, bottom-left, bottom-right) neighbors of `value`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]
[[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]
Output:
[null, 6, 16, 16, 4]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N^2)
- `adjacentSum`, `diagonalSum`: O(1)
Space Complexity: O(N^2) for coordinate lookup table.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map `value -> (r, c)`.
For `adjacentSum`: check `(r-1, c), (r+1, c), (r, c-1), (r, c+1)`.
For `diagonalSum`: check `(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)`.
"""

import unittest
class NeighborSum:
    """Grid neighbor summation service."""

    def __init__(self, grid: list[list[int]]) -> None:
        self.grid: list[list[int]] = grid
        self.n: int = len(grid)
        self.pos: dict[int, tuple[int, int]] = {}
        for r in range(self.n):
            for c in range(self.n):
                self.pos[grid[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        r, c = self.pos[value]
        total = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                total += self.grid[nr][nc]
        return total

    def diagonalSum(self, value: int) -> int:
        r, c = self.pos[value]
        total = 0
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                total += self.grid[nr][nc]
        return total
class TestNeighborSum(unittest.TestCase):
    def test_example_1(self) -> None:
        ns = NeighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual(ns.adjacentSum(1), 6)
        self.assertEqual(ns.adjacentSum(4), 16)
        self.assertEqual(ns.diagonalSum(4), 16)
        self.assertEqual(ns.diagonalSum(8), 4)


if __name__ == "__main__":
    unittest.main()
