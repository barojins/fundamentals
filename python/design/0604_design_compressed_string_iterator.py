"""
LeetCode 604: Design Compressed String Iterator
Difficulty: Easy
Tags: Array, String, Design, Iterator

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter being repeated in the original uncompressed string.

Implement the `StringIterator` class:
- `StringIterator(String compressedString)` Initializes the object with the compressed string.
- `char next()` Returns the next character, or `' '` if the original string has no more characters.
- `boolean hasNext()` Returns `true` if there is any character in the original string, and `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
Output:
[null, "L", "e", "e", "t", "C", "o", true, "d", true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next()`, `hasNext()`: O(1) amortized
Space Complexity: O(1) auxiliary space (reading directly from compressed string).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Parse the string lazily on demand:
- Maintain `index: int`, `curr_char: str`, and `curr_count: int`.
- When `curr_count == 0` and `index < len(compressedString)`:
  - Read `curr_char = s[index]`
  - Parse full multi-digit integer count following `curr_char`
  - Advance `index` past the digits.
"""

import unittest
class StringIterator:
    """Lazy iterator over Run-Length Encoded (RLE) compressed string."""

    def __init__(self, compressedString: str) -> None:
        self.s: str = compressedString
        self.idx: int = 0
        self.curr_char: str = " "
        self.curr_count: int = 0

    def _advance(self) -> None:
        if self.curr_count == 0 and self.idx < len(self.s):
            self.curr_char = self.s[self.idx]
            self.idx += 1
            num_start = self.idx
            while self.idx < len(self.s) and self.s[self.idx].isdigit():
                self.idx += 1
            self.curr_count = int(self.s[num_start : self.idx])

    def next(self) -> str:
        if not self.hasNext():
            return " "
        self.curr_count -= 1
        return self.curr_char

    def hasNext(self) -> bool:
        self._advance()
        return self.curr_count > 0
class TestStringIterator(unittest.TestCase):
    def test_example_1(self) -> None:
        iterator = StringIterator("L1e2t1C1o1d1e1")
        self.assertEqual(iterator.next(), "L")
        self.assertEqual(iterator.next(), "e")
        self.assertEqual(iterator.next(), "e")
        self.assertEqual(iterator.next(), "t")
        self.assertEqual(iterator.next(), "C")
        self.assertEqual(iterator.next(), "o")
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), "d")
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), "e")
        self.assertFalse(iterator.hasNext())
        self.assertEqual(iterator.next(), " ")


if __name__ == "__main__":
    unittest.main()
