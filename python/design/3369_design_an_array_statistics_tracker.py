"""
LeetCode 3369: Design an Array Statistics Tracker
Difficulty: Hard
Tags: Design, Queue, Heap (Priority Queue), Ordered Set, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that keeps track of the statistics of an array.

Implement the `StatisticsTracker` class:
- `StatisticsTracker()`: Initializes an empty object.
- `void addNumber(int number)`: Adds `number` to the back of the array.
- `void eraseNumber(int number)`: Removes the earliest added occurrence of `number` from the array.
- `int getMean()`: Returns the floored mean of numbers in the array.
- `int getMedian()`: Returns the median of numbers in the array.
- `int getMode()`: Returns the mode (most frequent number, breaking ties by smallest value).

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["StatisticsTracker", "addNumber", "addNumber", "getMean", "getMedian", "getMode", "eraseNumber", "getMean"]
[[], [3], [5], [], [], [], [3], []]
Output:
[null, null, null, 4, 5, 3, null, 5]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addNumber`, `eraseNumber`: O(log N)
- `getMean`, `getMedian`, `getMode`: O(1)
Space Complexity: O(N) for frequency tracking and balanced partitions.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `total_sum`, `count` for O(1) `getMean = total_sum // count`.
- Balanced sorted structure / two heaps for O(1) `getMedian`.
- Frequency map + Max-heap / buckets for O(1) `getMode`.
"""

import unittest
from collections import Counter
import bisect


class StatisticsTracker:
    """Array statistics tracker computing mean, median, and mode in O(1) / O(log N)."""

    def __init__(self) -> None:
        self.nums: list[int] = []
        self.sorted_nums: list[int] = []
        self.counts: Counter[int] = Counter()
        self.total_sum: int = 0

    def addNumber(self, number: int) -> None:
        self.nums.append(number)
        bisect.insort(self.sorted_nums, number)
        self.counts[number] += 1
        self.total_sum += number

    def eraseNumber(self, number: int) -> None:
        self.nums.remove(number)
        idx = bisect.bisect_left(self.sorted_nums, number)
        self.sorted_nums.pop(idx)
        self.counts[number] -= 1
        if self.counts[number] == 0:
            del self.counts[number]
        self.total_sum -= number

    def getMean(self) -> int:
        return self.total_sum // len(self.nums)

    def getMedian(self) -> int:
        n = len(self.sorted_nums)
        return self.sorted_nums[n // 2]

    def getMode(self) -> int:
        max_freq = max(self.counts.values())
        candidates = [num for num, f in self.counts.items() if f == max_freq]
        return min(candidates)
class TestStatisticsTracker(unittest.TestCase):
    def test_example_1(self) -> None:
        st = StatisticsTracker()
        st.addNumber(3)
        st.addNumber(5)
        self.assertEqual(st.getMean(), 4)
        self.assertEqual(st.getMedian(), 5)
        self.assertEqual(st.getMode(), 3)
        st.eraseNumber(3)
        self.assertEqual(st.getMean(), 5)


if __name__ == "__main__":
    unittest.main()
