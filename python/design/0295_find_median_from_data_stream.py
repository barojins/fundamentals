"""
LeetCode 295: Find Median from Data Stream
Difficulty: Hard
Tags: Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Find median from a continuous stream of numbers.

Implement `MedianFinder`:
- `void addNum(int num)`
- `double findMedian()`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addNum`: O(log N)
- `findMedian`: O(1)
Space Complexity: O(N)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Two heaps: max-heap `small` for lower half, min-heap `large` for upper half.
"""

import heapq
import unittest


class MedianFinder:
    """Finds running median from data stream using two heaps."""

    def __init__(self) -> None:
        self.small: list[int] = []  # Max-heap (inverted values)
        self.large: list[int] = []  # Min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


class TestMedianFinder(unittest.TestCase):
    def test_example_1(self) -> None:
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2.0)

    def test_negative_and_duplicates(self) -> None:
        mf = MedianFinder()
        mf.addNum(-1)
        self.assertEqual(mf.findMedian(), -1.0)
        mf.addNum(-2)
        self.assertEqual(mf.findMedian(), -1.5)
        mf.addNum(-3)
        self.assertEqual(mf.findMedian(), -2.0)


if __name__ == "__main__":
    unittest.main()
