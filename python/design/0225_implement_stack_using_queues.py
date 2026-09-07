"""
LeetCode 225: Implement Stack using Queues
Difficulty: Easy
Tags: Stack, Design, Queue

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Implement a last-in-first-out (LIFO) stack using only two queues (or one queue).

Implement the `MyStack` class:
- `void push(int x)` Pushes element x to top.
- `int pop()` Removes top element and returns it.
- `int top()` Returns top element.
- `boolean empty()` Returns `true` if stack is empty.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 2, 2, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `push`: O(N) rotation
- `pop`, `top`, `empty`: O(1)
Space Complexity: O(N)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
On `push(x)`: Append `x`, then rotate preceding `len - 1` elements to back.
"""

import unittest
from collections import deque


class MyStack:
    """LIFO Stack implemented using a single queue."""

    def __init__(self) -> None:
        self.queue: deque[int] = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


class TestMyStack(unittest.TestCase):
    def test_example_1(self) -> None:
        st = MyStack()
        st.push(1)
        st.push(2)
        self.assertEqual(st.top(), 2)
        self.assertEqual(st.pop(), 2)
        self.assertFalse(st.empty())
        self.assertEqual(st.pop(), 1)
        self.assertTrue(st.empty())

    def test_sequential_pushes(self) -> None:
        st = MyStack()
        for i in range(1, 6):
            st.push(i)
        for i in range(5, 0, -1):
            self.assertEqual(st.pop(), i)


if __name__ == "__main__":
    unittest.main()
