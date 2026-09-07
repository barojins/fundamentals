"""
LeetCode 1429: First Unique Number
Difficulty: Medium
Tags: Array, Hash Table, Design, Queue, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the `FirstUnique` class:
- `FirstUnique(int[] nums)` Initializes the object with the numbers in the queue.
- `int showFirstUnique()` returns the value of the first unique integer of the queue, and returns `-1` if there is no such integer.
- `void add(int value)` insert `value` to the queue.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `showFirstUnique`: O(1) amortized
- `add`: O(1)
Space Complexity: O(N) to store frequencies and queue.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `counts: Counter[int]`
- `queue: deque[int]` of numbers seen so far.
On `showFirstUnique()`:
- While `queue` is non-empty and `counts[queue[0]] > 1`: pop from left.
- If queue is empty, return -1; else return `queue[0]`.
"""

import unittest
from collections import Counter, deque


class FirstUnique:
    """First unique number finder using sliding queue with lazy frequency eviction."""

    def __init__(self, nums: list[int]) -> None:
        self.counts: Counter[int] = Counter(nums)
        self.queue: deque[int] = deque(nums)

    def showFirstUnique(self) -> int:
        while self.queue and self.counts[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        self.counts[value] += 1
        self.queue.append(value)
class TestFirstUnique(unittest.TestCase):
    def test_example_1(self) -> None:
        fu = FirstUnique([2, 3, 5])
        self.assertEqual(fu.showFirstUnique(), 2)
        fu.add(5)
        self.assertEqual(fu.showFirstUnique(), 2)
        fu.add(2)
        self.assertEqual(fu.showFirstUnique(), 3)
        fu.add(3)
        self.assertEqual(fu.showFirstUnique(), -1)


if __name__ == "__main__":
    unittest.main()
