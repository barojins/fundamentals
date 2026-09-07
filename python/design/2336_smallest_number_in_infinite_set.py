"""
LeetCode 2336: Smallest Number in Infinite Set
Difficulty: Medium
Tags: Hash Table, Design, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You have a set which contains all positive integers `[1, 2, 3, 4, 5, ...]`.

Implement the `SmallestInfiniteSet` class:
- `SmallestInfiniteSet()` Initializes the SmallestInfiniteSet object to contain all positive integers.
- `int popSmallest()` Removes and returns the smallest integer contained in the infinite set.
- `void addBack(int num)` Adds a positive integer `num` back into the infinite set, if it is not already in the infinite set.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output:
[null, null, 1, 2, 3, null, 1, 4, 5]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `popSmallest`, `addBack`: O(log N)
Space Complexity: O(N) for added-back elements.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `current: int = 1` (the smallest contiguous integer not yet popped)
- `added_back_heap: list[int]` min-heap of numbers `< current` added back.
- `added_back_set: set[int]` to avoid duplicate additions.
"""

import unittest
import heapq


class SmallestInfiniteSet:
    """Infinite positive integer set with minimum extraction and re-addition."""

    def __init__(self) -> None:
        self.current: int = 1
        self.added_heap: list[int] = []
        self.added_set: set[int] = set()

    def popSmallest(self) -> int:
        if self.added_heap:
            val = heapq.heappop(self.added_heap)
            self.added_set.remove(val)
            return val
        val = self.current
        self.current += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_set:
            self.added_set.add(num)
            heapq.heappush(self.added_heap, num)
class TestSmallestInfiniteSet(unittest.TestCase):
    def test_example_1(self) -> None:
        sis = SmallestInfiniteSet()
        sis.addBack(2)
        self.assertEqual(sis.popSmallest(), 1)
        self.assertEqual(sis.popSmallest(), 2)
        self.assertEqual(sis.popSmallest(), 3)
        sis.addBack(1)
        self.assertEqual(sis.popSmallest(), 1)
        self.assertEqual(sis.popSmallest(), 4)
        self.assertEqual(sis.popSmallest(), 5)


if __name__ == "__main__":
    unittest.main()
