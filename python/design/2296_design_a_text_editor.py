"""
LeetCode 2296: Design a Text Editor
Difficulty: Hard
Tags: Linked List, String, Stack, Design, Doubly-Linked List, Simulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a text editor with a cursor that can do the following:
- `addText(string text)` Appends text to where the cursor is.
- `deleteText(int k)` Deletes `k` characters to the left of the cursor. Returns the actual number of characters deleted.
- `cursorLeft(int k)` Moves cursor `k` times to the left. Returns the last `min(10, len)` characters to the left of the cursor.
- `cursorRight(int k)` Moves cursor `k` times to the right. Returns the last `min(10, len)` characters to the left of the cursor.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
Output:
[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addText`: O(len(text))
- `deleteText`: O(min(k, len(left)))
- `cursorLeft`, `cursorRight`: O(min(k, len))
Space Complexity: O(Total characters in text editor).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use two stacks (Gap Buffer / Two Stacks):
- `left: list[str]` (characters to the left of cursor)
- `right: list[str]` (characters to the right of cursor in reverse order)
Moving left pops from `left` and appends to `right`.
Moving right pops from `right` and appends to `left`.
"""

import unittest
class TextEditor:
    """Text editor with cursor using dual character stacks."""

    def __init__(self) -> None:
        self.left: list[str] = []
        self.right: list[str] = []

    def addText(self, text: str) -> None:
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
        deleted = min(k, len(self.left))
        for _ in range(deleted):
            self.left.pop()
        return deleted

    def _get_left_10(self) -> str:
        return "".join(self.left[-min(10, len(self.left)) :])

    def cursorLeft(self, k: int) -> str:
        steps = min(k, len(self.left))
        for _ in range(steps):
            self.right.append(self.left.pop())
        return self._get_left_10()

    def cursorRight(self, k: int) -> str:
        steps = min(k, len(self.right))
        for _ in range(steps):
            self.left.append(self.right.pop())
        return self._get_left_10()
class TestTextEditor(unittest.TestCase):
    def test_example_1(self) -> None:
        te = TextEditor()
        te.addText("leetcode")
        self.assertEqual(te.deleteText(4), 4)
        te.addText("practice")
        self.assertEqual(te.cursorRight(3), "etpractice")
        self.assertEqual(te.cursorLeft(8), "leet")
        self.assertEqual(te.deleteText(10), 4)
        self.assertEqual(te.cursorLeft(2), "")
        self.assertEqual(te.cursorRight(6), "practi")


if __name__ == "__main__":
    unittest.main()
