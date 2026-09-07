"""
LeetCode 3484: Design Spreadsheet
Difficulty: Medium
Tags: Array, Hash Table, Design, Matrix

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a spreadsheet that can set cell values, reset them, and compute sums.

Implement the `Spreadsheet` class:
- `Spreadsheet(int rows)`
- `void setCell(string cell, int value)`
- `void resetCell(string cell)`
- `int getCellValue(string cell)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Spreadsheet", "setCell", "getCellValue", "resetCell", "getCellValue"]
[[10], ["A1", 42], ["A1"], ["A1"], ["A1"]]
Output:
[null, null, 42, null, 0]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `setCell`, `resetCell`, `getCellValue`: O(1)
Space Complexity: O(Non-zero cells).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map `cell_name -> value: dict[str, int]`.
`resetCell` removes the cell from dictionary, and `getCellValue` defaults to `0`.
"""

import unittest
class Spreadsheet:
    """Spreadsheet grid cell manager."""

    def __init__(self, rows: int) -> None:
        self.rows: int = rows
        self.cells: dict[str, int] = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getCellValue(self, cell: str) -> int:
        return self.cells.get(cell, 0)
class TestSpreadsheet(unittest.TestCase):
    def test_example_1(self) -> None:
        ss = Spreadsheet(10)
        ss.setCell("A1", 42)
        self.assertEqual(ss.getCellValue("A1"), 42)
        ss.resetCell("A1")
        self.assertEqual(ss.getCellValue("A1"), 0)


if __name__ == "__main__":
    unittest.main()
