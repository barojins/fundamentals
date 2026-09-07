"""
LeetCode 1476: Subrectangle Queries
Difficulty: Medium
Tags: Array, Design, Matrix

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Implement the class `SubrectangleQueries` which receives a `rows x cols` rectangle of integers and supports two operations:
1. `updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)`: Updates all values with `newValue` in the subrectangle whose upper left coordinate is `(row1,col1)` and bottom right coordinate is `(row2,col2)`.
2. `getValue(int row, int col)`: Returns the current value of the coordinate `(row,col)` from the rectangle.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
Output:
[null,1,null,5,5,null,10,5]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `updateSubrectangle`: O(1) recording update history!
- `getValue`: O(U) where U is number of updates (scanning updates backwards).
Space Complexity: O(R * C + U) for grid and update history.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Record each update operation `(r1, c1, r2, c2, val)` in an `updates` list.
On `getValue(r, c)`:
Scan `updates` in reverse order: the first update containing `(r, c)` returns its value. If none match, return original `grid[r][c]`.
"""

import unittest
class SubrectangleQueries:
    """Subrectangle matrix queries with O(1) lazy history updates."""

    def __init__(self, rectangle: list[list[int]]) -> None:
        self.grid: list[list[int]] = [row[:] for row in rectangle]
        self.updates: list[tuple[int, int, int, int, int]] = []

    def updateSubrectangle(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int,
        newValue: int,
    ) -> None:
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for r1, c1, r2, c2, val in reversed(self.updates):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        return self.grid[row][col]
class TestSubrectangleQueries(unittest.TestCase):
    def test_example_1(self) -> None:
        sq = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
        self.assertEqual(sq.getValue(0, 2), 1)
        sq.updateSubrectangle(0, 0, 3, 2, 5)
        self.assertEqual(sq.getValue(0, 2), 5)
        self.assertEqual(sq.getValue(3, 1), 5)
        sq.updateSubrectangle(3, 0, 3, 2, 10)
        self.assertEqual(sq.getValue(3, 1), 10)
        self.assertEqual(sq.getValue(0, 2), 5)


if __name__ == "__main__":
    unittest.main()
