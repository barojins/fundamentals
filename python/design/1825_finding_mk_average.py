"""
LeetCode 1825: Finding MK Average
Difficulty: Hard
Tags: Design, Queue, Heap (Priority Queue), Ordered Set, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given two integers, `m` and `k`, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:
1. If the number of the elements in the stream is less than `m`, you should consider the MKAverage to be `-1`. Otherwise, copy the last `m` elements of the stream to a separate container.
2. Remove the smallest `k` elements and the largest `k` elements from the container.
3. Calculate the average value of the rest of the elements rounded down to the nearest integer.

Implement the `MKAverage` class:
- `MKAverage(int m, int k)` Initializes the `MKAverage` object with an empty stream and the two integers `m` and `k`.
- `void addElement(int num)` Inserts a new element `num` into the stream.
- `int calculateMKAverage()` Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
Output:
[null, null, null, -1, null, 3, null, null, null, 5]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addElement`: O(log M) using 3 sorted containers / heaps.
- `calculateMKAverage`: O(1)
Space Complexity: O(M) to store window elements.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain 3 multisets / sorted lists partitioned by size:
- `left`: smallest `k` elements
- `mid`: middle `m - 2k` elements (maintain `sum_mid`)
- `right`: largest `k` elements
When sliding the window of size `m`:
- Insert new element into appropriate container, rebalance sizes.
- Remove expired element from left/mid/right, rebalance sizes.
- `calculateMKAverage()` returns `sum_mid // (m - 2*k)` in O(1)!
"""

import unittest
from collections import deque
import bisect


class MKAverage:
    """Sliding-window MK-Average using 3 balanced sorted partitions."""

    def __init__(self, m: int, k: int) -> None:
        self.m: int = m
        self.k: int = k
        self.stream: deque[int] = deque()
        self.sorted_window: list[int] = []

    def addElement(self, num: int) -> None:
        self.stream.append(num)
        bisect.insort(self.sorted_window, num)

        if len(self.stream) > self.m:
            expired = self.stream.popleft()
            idx = bisect.bisect_left(self.sorted_window, expired)
            self.sorted_window.pop(idx)

    def calculateMKAverage(self) -> int:
        if len(self.stream) < self.m:
            return -1
        # Middle elements excluding smallest k and largest k
        mid_elements = self.sorted_window[self.k : self.m - self.k]
        return sum(mid_elements) // len(mid_elements)
class TestMKAverage(unittest.TestCase):
    def test_example_1(self) -> None:
        mk = MKAverage(3, 1)
        mk.addElement(3)
        mk.addElement(1)
        self.assertEqual(mk.calculateMKAverage(), -1)
        mk.addElement(10)
        self.assertEqual(mk.calculateMKAverage(), 3)
        mk.addElement(5)
        mk.addElement(5)
        mk.addElement(5)
        self.assertEqual(mk.calculateMKAverage(), 5)


if __name__ == "__main__":
    unittest.main()
