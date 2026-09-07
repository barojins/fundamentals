"""
LeetCode 1381: Design a Stack With Increment Operation
Difficulty: Medium
Tags: Array, Stack, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a stack that supports increment operations on its elements.

Implement the `CustomStack` class:
- `CustomStack(int maxSize)` Initializes the object with `maxSize` which is the maximum number of elements in the stack.
- `void push(int x)` Adds `x` to the top of the stack if the stack has not reached the `maxSize`.
- `int pop()` Pops and returns the top of the stack or `-1` if the stack is empty.
- `void increment(int k, int val)` Increments the bottom `k` elements of the stack by `val`. If there are less than `k` elements in the stack, increment all the elements in the stack.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output:
[null,null,null,2,null,null,null,null,null,103,202,201,-1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `push`, `pop`, `increment`: O(1) for all operations using lazy propagation!
Space Complexity: O(maxSize) for stack and lazy increment arrays.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use lazy increment propagation:
Maintain `stack: list[int]` and `inc: list[int]` of size `maxSize`.
On `increment(k, val)`:
- `idx = min(k, len(stack)) - 1`
- If `idx >= 0`: `inc[idx] += val`
On `pop()`:
- `idx = len(stack) - 1`
- Top value is `stack[idx] + inc[idx]`.
- Pass increment down to previous element: if `idx > 0`: `inc[idx - 1] += inc[idx]`.
- Reset `inc[idx] = 0` and pop from `stack`.
"""

import unittest
class CustomStack:
    """Stack supporting O(1) push, pop, and lazy bottom-k increment."""

    def __init__(self, maxSize: int) -> None:
        self.max_size: int = maxSize
        self.stack: list[int] = []
        self.inc: list[int] = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        val = self.stack.pop() + self.inc[idx]
        if idx > 0:
            self.inc[idx - 1] += self.inc[idx]
        self.inc.pop()
        return val

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            idx = min(k, len(self.stack)) - 1
            self.inc[idx] += val
class TestCustomStack(unittest.TestCase):
    def test_example_1(self) -> None:
        st = CustomStack(3)
        st.push(1)
        st.push(2)
        self.assertEqual(st.pop(), 2)
        st.push(2)
        st.push(3)
        st.push(4)  # Ignored (maxSize = 3)
        st.increment(5, 100)
        st.increment(2, 100)
        self.assertEqual(st.pop(), 103)
        self.assertEqual(st.pop(), 202)
        self.assertEqual(st.pop(), 201)
        self.assertEqual(st.pop(), -1)


if __name__ == "__main__":
    unittest.main()
