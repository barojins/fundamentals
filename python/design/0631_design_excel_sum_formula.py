"""
LeetCode 631: Design Excel Sum Formula
Difficulty: Hard
Tags: Array, Hash Table, Design, Matrix, Graph, Topological Sort

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design the basic function of Excel and implement the formula of the sum function.

Implement the `Excel` class:
- `Excel(int height, char width)` Initializes the object with the `height` and the `width` of the sheet. The sheet is 1-indexed for height (`1` to `height`) and char-indexed for width (`'A'` to `width`).
- `void set(int row, char column, int val)` Sets the value present at `(row, column)` to `val`.
- `int get(int row, char column)` Returns the value present at `(row, column)`.
- `int sum(int row, char column, String[] numbers)` Sets the value at `(row, column)` to the sum of the cells represented by `numbers` and returns the value at `(row, column)`. `numbers` is an array of strings representing cell coordinates (e.g., `"A1"`) or ranges (e.g., `"A1:B2"`). This formula remains active and recalculated upon subsequent `get` calls.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "2", 2], [3, "C"]]
Output:
[null, null, 4, null, 6]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `set`: O(1)
- `sum`: O(number of cells referenced)
- `get`: O(V + E) evaluation of formula dependency graph.
Space Complexity: O(height * width) to store cell values and formula dependency multiset.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store each cell with either:
- A direct raw `val: int`
- Or a formula map `Counter[(r, c)]` of cell dependencies.
On `get(r, c)`: recursively calculate sum of dependent cells times their multiplicities.
"""

import unittest
from collections import Counter


class Excel:
    """Spreadsheet with recursive formula evaluation."""

    def __init__(self, height: int, width: str) -> None:
        self.H = height
        self.W = ord(width) - ord("A") + 1
        # Store either int or Counter[tuple[int, int]]
        self.cells: dict[tuple[int, int], int | Counter[tuple[int, int]]] = {}

    def _pos(self, row: int, col_char: str) -> tuple[int, int]:
        return row, ord(col_char) - ord("A")

    def set(self, row: int, column: str, val: int) -> None:
        pos = self._pos(row, column)
        self.cells[pos] = val

    def get(self, row: int, column: str) -> int:
        pos = self._pos(row, column)
        return self._eval(pos)

    def _eval(self, pos: tuple[int, int]) -> int:
        if pos not in self.cells:
            return 0
        val = self.cells[pos]
        if isinstance(val, int):
            return val
        # Formula: val is Counter of dependent cell positions
        total = 0
        for dep_pos, count in val.items():
            total += count * self._eval(dep_pos)
        return total

    def sum(self, row: int, column: str, numbers: list[str]) -> int:
        pos = self._pos(row, column)
        formula = Counter[tuple[int, int]]()

        for token in numbers:
            if ":" in token:
                top_left, bottom_right = token.split(":")
                r1, c1 = int(top_left[1:]), ord(top_left[0]) - ord("A")
                r2, c2 = int(bottom_right[1:]), ord(bottom_right[0]) - ord("A")
                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        formula[(r, c)] += 1
            else:
                r, c = int(token[1:]), ord(token[0]) - ord("A")
                formula[(r, c)] += 1

        self.cells[pos] = formula
        return self._eval(pos)
class TestExcel(unittest.TestCase):
    def test_example_1(self) -> None:
        excel = Excel(3, "C")
        excel.set(1, "A", 2)
        self.assertEqual(excel.sum(3, "C", ["A1", "A1:B2"]), 4)
        excel.set(2, "B", 2)
        self.assertEqual(excel.get(3, "C"), 6)


if __name__ == "__main__":
    unittest.main()
