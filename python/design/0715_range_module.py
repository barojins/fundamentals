"""
LeetCode 715: Range Module
Difficulty: Hard
Tags: Design, Segment Tree, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A Range Module is a module that tracks ranges of numbers. Design a data structure to track and query half-open intervals `[left, right)`.

Implement the `RangeModule` class:
- `RangeModule()` Initializes the object of the data structure.
- `void addRange(int left, int right)` Adds the half-open interval `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should extend the tracking.
- `boolean queryRange(int left, int right)` Returns `true` if every real number in `[left, right)` is currently being tracked, and `false` otherwise.
- `void removeRange(int left, int right)` Stops tracking every real number currently being tracked in the half-open interval `[left, right)`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output:
[null, null, null, true, false, true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addRange`, `removeRange`: O(N) where N is number of disjoint intervals.
- `queryRange`: O(log N) using binary search.
Space Complexity: O(N) to store non-overlapping sorted intervals.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store intervals in a sorted list `intervals: list[list[int]]`.
- `addRange(left, right)`: find overlapping intervals, expand `[left, right]` to cover them, and replace overlapping sub-array with the merged single interval.
- `removeRange(left, right)`: trim or split any overlapping intervals.
- `queryRange(left, right)`: binary search (`bisect_right`) to find interval with start <= left, then verify its `end >= right`.
"""

import unittest
import bisect


class RangeModule:
    """Tracks and queries tracked half-open intervals [left, right)."""

    def __init__(self) -> None:
        self.intervals: list[list[int]] = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        placed = False
        for iv in self.intervals:
            if iv[1] < left:
                new_intervals.append(iv)
            elif iv[0] > right:
                if not placed:
                    new_intervals.append([left, right])
                    placed = True
                new_intervals.append(iv)
            else:
                left = min(left, iv[0])
                right = max(right, iv[1])

        if not placed:
            new_intervals.append([left, right])
        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        idx = bisect.bisect_right(self.intervals, [left, float("inf")]) - 1
        if idx < 0:
            return False
        return self.intervals[idx][0] <= left and self.intervals[idx][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        for iv in self.intervals:
            if iv[1] <= left or iv[0] >= right:
                new_intervals.append(iv)
            else:
                if iv[0] < left:
                    new_intervals.append([iv[0], left])
                if iv[1] > right:
                    new_intervals.append([right, iv[1]])
        self.intervals = new_intervals
class TestRangeModule(unittest.TestCase):
    def test_example_1(self) -> None:
        rm = RangeModule()
        rm.addRange(10, 20)
        rm.removeRange(14, 16)
        self.assertTrue(rm.queryRange(10, 14))
        self.assertFalse(rm.queryRange(13, 15))
        self.assertTrue(rm.queryRange(16, 17))


if __name__ == "__main__":
    unittest.main()
