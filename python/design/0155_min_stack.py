"""
LeetCode 155: Min Stack
Difficulty: Medium
Tags: Stack, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `push`, `pop`, `top`, `getMin`: O(1) for all operations.
Space Complexity: O(N) where N is the number of elements in the stack.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store pairs of `(val, current_min)` on a single stack, or maintain a secondary `min_stack` where each entry tracks the minimum value at that depth.
"""

import unittest


class MinStack:
    """Stack supporting O(1) retrieval of minimum element."""

    def __init__(self) -> None:
        self.stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        curr_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty MinStack")
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("getMin from empty MinStack")
        return self.stack[-1][1]


class TestMinStack(unittest.TestCase):
    def test_example_1(self) -> None:
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3)
        minStack.pop()
        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.getMin(), -2)

    def test_duplicate_minimums(self) -> None:
        ms = MinStack()
        ms.push(2)
        ms.push(0)
        ms.push(3)
        ms.push(0)
        self.assertEqual(ms.getMin(), 0)
        ms.pop()
        self.assertEqual(ms.getMin(), 0)
        ms.pop()
        self.assertEqual(ms.getMin(), 0)
        ms.pop()
        self.assertEqual(ms.getMin(), 2)

    def test_monotonic_sequences(self) -> None:
        ms = MinStack()
        for x in [5, 4, 3, 2, 1]:
            ms.push(x)
            self.assertEqual(ms.getMin(), x)
        for x in [1, 2, 3, 4, 5]:
            self.assertEqual(ms.top(), x)
            self.assertEqual(ms.getMin(), x)
            ms.pop()


if __name__ == "__main__":
    unittest.main()
