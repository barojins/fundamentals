"""
LeetCode 2408: Design SQL
Difficulty: Medium
Tags: Array, Hash Table, String, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given `n` tables represented with two arrays `names` and `columns`, where `names[i]` is the name of the `i-th` table and `columns[i]` is the number of columns of the `i-th` table.

Implement the `SQL` class:
- `SQL(String[] names, int[] columns)`
- `void insertRow(String name, String[] row)` Adds a row to table `name` with auto-incrementing 1-based `rowId`.
- `void deleteRow(String name, int rowId)` Deletes the row with `rowId` from table `name`.
- `String selectCell(String name, int rowId, int columnId)` Returns cell value (1-indexed columnId).

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["SQL", "insertRow", "selectCell", "insertRow", "deleteRow", "selectCell"]
[[["one", "two"], [2, 3]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", ["fourth", "fifth", "sixth"]], ["two", 1], ["two", 2, 2]]
Output:
[null, null, "third", null, null, "fifth"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `insertRow`, `deleteRow`, `selectCell`: O(1)
Space Complexity: O(Total rows inserted).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Each table has:
- `next_id: int` auto-incrementing ID.
- `rows: dict[int, list[str]]` mapping `rowId -> row_values`.
"""

import unittest
class Table:
    def __init__(self, name: str, columns: int) -> None:
        self.name: str = name
        self.columns: int = columns
        self.rows: dict[int, list[str]] = {}
        self.next_id: int = 1


class SQL:
    """In-memory SQL table store with auto-incrementing row keys."""

    def __init__(self, names: list[str], columns: list[int]) -> None:
        self.tables: dict[str, Table] = {
            name: Table(name, col) for name, col in zip(names, columns)
        }

    def insertRow(self, name: str, row: list[str]) -> None:
        table = self.tables[name]
        table.rows[table.next_id] = row
        table.next_id += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        table = self.tables[name]
        if rowId in table.rows:
            del table.rows[rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables[name]
        return table.rows[rowId][columnId - 1]
class TestSQL(unittest.TestCase):
    def test_example_1(self) -> None:
        sql = SQL(["one", "two"], [2, 3])
        sql.insertRow("two", ["first", "second", "third"])
        self.assertEqual(sql.selectCell("two", 1, 3), "third")
        sql.insertRow("two", ["fourth", "fifth", "sixth"])
        sql.deleteRow("two", 1)
        self.assertEqual(sql.selectCell("two", 2, 2), "fifth")


if __name__ == "__main__":
    unittest.main()
