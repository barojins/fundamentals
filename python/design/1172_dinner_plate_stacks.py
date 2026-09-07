"""
LeetCode 1172: Dinner Plate Stacks
Difficulty: Hard
Tags: Hash Table, Stack, Design, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You have an infinite number of stacks arranged in an orderly line, numbered `0` to `infinity` from left to right. Each stack has the same maximum `capacity`.

Implement the `DinnerPlates` class:
- `DinnerPlates(int capacity)` Initializes the object with the maximum `capacity` of the stacks.
- `void push(int val)` Pushes the given integer `val` into the leftmost stack with size less than `capacity`.
- `int pop()` Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns `-1` if all stacks are empty.
- `int popAtStack(int index)` Returns the value at the top of the stack with the given `index` and removes it from that stack, and returns `-1` if the stack with an `index` is empty.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
Output:
[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `push`: O(log S) using min-heap of available stack indices.
- `pop`: O(1) amortized
- `popAtStack(index)`: O(log S)
Space Complexity: O(N) to store plates.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `stacks: list[list[int]]`
- `available_heap: list[int]` min-heap of stack indices with size < capacity.
On `push(val)`:
- Clean up `available_heap` (discard indices >= len(stacks)).
- If heap is empty, append a new stack to `stacks`.
- Push to target stack; if it still has capacity, push index back to heap.
On `pop()`: pop from `popAtStack(len(stacks) - 1)` trimming trailing empty stacks.
"""

import unittest
import heapq


class DinnerPlates:
    """Dinner plate stack manager with O(log S) push and popAtStack."""

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.stacks: list[list[int]] = []
        self.available: list[int] = []  # Min-heap of indices with free space

    def push(self, val: int) -> None:
        while self.available and self.available[0] < len(self.stacks) and len(self.stacks[self.available[0]]) == self.capacity:
            heapq.heappop(self.available)

        if not self.available:
            self.stacks.append([val])
            if self.capacity > 1:
                heapq.heappush(self.available, len(self.stacks) - 1)
        else:
            idx = heapq.heappop(self.available)
            if idx >= len(self.stacks):
                self.stacks.append([val])
            else:
                self.stacks[idx].append(val)
            if len(self.stacks[idx]) < self.capacity:
                heapq.heappush(self.available, idx)

    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()
        heapq.heappush(self.available, index)

        # Trim trailing empty stacks
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val

class TestDinnerPlates(unittest.TestCase):
    def test_example_1(self) -> None:
        dp = DinnerPlates(2)
        for x in [1, 2, 3, 4, 5]:
            dp.push(x)
        self.assertEqual(dp.popAtStack(0), 2)
        dp.push(20)
        dp.push(21)
        self.assertEqual(dp.popAtStack(0), 20)
        self.assertEqual(dp.popAtStack(2), 21)
        self.assertEqual(dp.pop(), 5)
        self.assertEqual(dp.pop(), 4)
        self.assertEqual(dp.pop(), 3)
        self.assertEqual(dp.pop(), 1)
        self.assertEqual(dp.pop(), -1)


if __name__ == "__main__":
    unittest.main()
