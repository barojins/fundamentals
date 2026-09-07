"""
LeetCode 232: Implement Queue using Stacks
Difficulty: Easy
Tags: Stack, Design, Queue

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Implement a first in first out (FIFO) queue using only two stacks with amortized O(1) operations.

Implement the `MyQueue` class:
- `void push(int x)` Pushes element x to back.
- `int pop()` Removes front element and returns it.
- `int peek()` Returns front element.
- `boolean empty()` Returns `true` if queue is empty.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 1, 1, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `push`: O(1)
- `pop`, `peek`: O(1) amortized
- `empty`: O(1)
Space Complexity: O(N)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use `in_stack` and `out_stack`. On pop/peek, transfer from in to out if out is empty.
"""

import unittest


class MyQueue:
    """FIFO Queue implemented using two stacks with amortized O(1) operations."""

    def __init__(self) -> None:
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def _move(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


class TestMyQueue(unittest.TestCase):
    def test_example_1(self) -> None:
        q = MyQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)
        self.assertFalse(q.empty())
        self.assertEqual(q.pop(), 2)
        self.assertTrue(q.empty())

    def test_interleaved_push_pop(self) -> None:
        q = MyQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        q.push(3)
        self.assertEqual(q.pop(), 2)
        self.assertEqual(q.pop(), 3)
        self.assertTrue(q.empty())


if __name__ == "__main__":
    unittest.main()
