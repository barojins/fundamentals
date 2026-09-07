"""
LeetCode 284: Peeking Iterator
Difficulty: Medium
Tags: Array, Design, Iterator

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an iterator that supports the `peek` operation on an existing iterator.

Implement the `PeekingIterator` class:
- `PeekingIterator(Iterator<int> nums)`
- `int peek()`
- `int next()`
- `boolean hasNext()`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output:
[null, 1, 2, 2, 3, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `peek`, `next`, `hasNext`: O(1)
Space Complexity: O(1)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Buffer the next value in `self._next_val`.
"""

import unittest
from collections.abc import Iterator


class PeekingIterator:
    """Iterator wrapper that supports O(1) peek() without advancing cursor."""

    def __init__(self, iterator: Iterator[int]) -> None:
        self.iterator = iterator
        self._next_val: int | None = None
        self._has_next: bool = False
        self._advance()

    def _advance(self) -> None:
        try:
            self._next_val = next(self.iterator)
            self._has_next = True
        except StopIteration:
            self._next_val = None
            self._has_next = False

    def peek(self) -> int:
        if not self._has_next or self._next_val is None:
            raise StopIteration("peek on exhausted iterator")
        return self._next_val

    def next(self) -> int:
        if not self._has_next or self._next_val is None:
            raise StopIteration("next on exhausted iterator")
        val = self._next_val
        self._advance()
        return val

    def hasNext(self) -> bool:
        return self._has_next


class TestPeekingIterator(unittest.TestCase):
    def test_example_1(self) -> None:
        nums = iter([1, 2, 3])
        pi = PeekingIterator(nums)
        self.assertEqual(pi.next(), 1)
        self.assertEqual(pi.peek(), 2)
        self.assertEqual(pi.next(), 2)
        self.assertEqual(pi.next(), 3)
        self.assertFalse(pi.hasNext())

    def test_multiple_peeks(self) -> None:
        nums = iter([10, 20])
        pi = PeekingIterator(nums)
        self.assertEqual(pi.peek(), 10)
        self.assertEqual(pi.peek(), 10)
        self.assertEqual(pi.next(), 10)
        self.assertEqual(pi.peek(), 20)
        self.assertEqual(pi.next(), 20)
        self.assertFalse(pi.hasNext())


if __name__ == "__main__":
    unittest.main()
