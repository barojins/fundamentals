"""
LeetCode 1670: Design Front Middle Back Queue
Difficulty: Medium
Tags: Array, Linked List, Design, Queue, Doubly-Linked List, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a queue that supports `push` and `pop` operations in the front, middle, and back.

Implement the `FrontMiddleBackQueue` class:
- `FrontMiddleBackQueue()` Initializes the queue.
- `void pushFront(int val)` Adds `val` to the front of the queue.
- `void pushMiddle(int val)` Adds `val` to the middle of the queue.
- `void pushBack(int val)` Adds `val` to the back of the queue.
- `int popFront()` Removes the front element of the queue and returns it. If the queue is empty, returns `-1`.
- `int popMiddle()` Removes the middle element of the queue and returns it. If the queue is empty, returns `-1`.
- `int popBack()` Removes the back element of the queue and returns it. If the queue is empty, returns `-1`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- All operations (`pushFront`, `pushMiddle`, `pushBack`, `popFront`, `popMiddle`, `popBack`): O(1)
Space Complexity: O(N) using two deques.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use two double-ended queues `left` and `right`.
Invariant: `len(left) == len(right)` or `len(left) == len(right) - 1`.
- Middle element is `left[-1]` if `len(left) == len(right)` else `right[0]`.
- Balance lengths after every push/pop to maintain invariant in O(1).
"""

import unittest
from collections import deque


class FrontMiddleBackQueue:
    """Queue supporting O(1) front, middle, and back push/pop using two balanced deques."""

    def __init__(self) -> None:
        self.left: deque[int] = deque()
        self.right: deque[int] = deque()

    def _balance(self) -> None:
        # Invariant: len(right) - 1 <= len(left) <= len(right)
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        val = self.left.popleft() if self.left else self.right.popleft()
        self._balance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        if len(self.left) == len(self.right):
            val = self.left.pop()
        else:
            val = self.right.popleft()
        self._balance()
        return val

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        val = self.right.pop()
        self._balance()
        return val
class TestFrontMiddleBackQueue(unittest.TestCase):
    def test_example_1(self) -> None:
        q = FrontMiddleBackQueue()
        q.pushFront(1)
        q.pushBack(2)
        q.pushMiddle(3)
        q.pushMiddle(4)
        self.assertEqual(q.popFront(), 1)
        self.assertEqual(q.popMiddle(), 3)
        self.assertEqual(q.popMiddle(), 4)
        self.assertEqual(q.popBack(), 2)
        self.assertEqual(q.popFront(), -1)


if __name__ == "__main__":
    unittest.main()
