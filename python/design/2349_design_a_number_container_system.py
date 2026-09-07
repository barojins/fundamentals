"""
LeetCode 2349: Design a Number Container System
Difficulty: Medium
Tags: Hash Table, Design, Heap (Priority Queue), Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a number container system that can do the following:
- Insert or Replace a number at the given index in the system.
- Return the smallest index for the given number in the system.

Implement the `NumberContainers` class:
- `NumberContainers()` Initializes the number container system.
- `void change(int index, int number)` Fills the container at index with the number.
- `int find(int number)` Returns the smallest index for the given number, or `-1` if no index exists.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output:
[null, -1, null, null, null, null, 1, null, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `change`: O(log N)
- `find`: O(1) amortized lazy heap cleanup.
Space Complexity: O(N) for indices map and min-heaps.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `index_to_num: dict[int, int]`
- `num_to_indices_heap: dict[int, list[int]]`
On `find(number)`:
Lazy-clean the heap by popping indices whose current value in `index_to_num` is no longer `number`.
"""

import unittest
from collections import defaultdict
import heapq


class NumberContainers:
    """Container tracking smallest index per number using min-heaps with lazy deletion."""

    def __init__(self) -> None:
        self.idx_to_num: dict[int, int] = {}
        self.num_to_heap: dict[int, list[int]] = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idx_to_num[index] = number
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_heap:
            return -1

        h = self.num_to_heap[number]
        while h:
            idx = h[0]
            if self.idx_to_num.get(idx) == number:
                return idx
            heapq.heappop(h)

        return -1
class TestNumberContainers(unittest.TestCase):
    def test_example_1(self) -> None:
        nc = NumberContainers()
        self.assertEqual(nc.find(10), -1)
        nc.change(2, 10)
        nc.change(1, 10)
        nc.change(3, 10)
        nc.change(5, 10)
        self.assertEqual(nc.find(10), 1)
        nc.change(1, 20)
        self.assertEqual(nc.find(10), 2)


if __name__ == "__main__":
    unittest.main()
