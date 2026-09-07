"""
LeetCode 2276: Count Integers in Intervals
Difficulty: Hard
Tags: Design, Segment Tree, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given an empty set of intervals, implement a data structure that can add new intervals and efficiently count the number of unique integers contained across all intervals.

Implement the `CountIntervals` class:
- `CountIntervals()` Initializes the object.
- `void add(int left, int right)` Adds the interval `[left, right]` to the set of intervals.
- `int count()` Returns the number of integers present in at least one interval.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
Output:
[null, null, null, 6, null, 8]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add`: O(log N) amortized per interval merge
- `count`: O(1)
Space Complexity: O(N) for disjoint intervals.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain disjoint sorted intervals `intervals: list[list[int]]` and running `self.total_count`.
When adding `[left, right]`:
Merge all overlapping / adjacent intervals `[l_i, r_i]`, subtract their length `(r_i - l_i + 1)` from `total_count`, compute merged boundary `[L, R]`, and add `(R - L + 1)` to `total_count`.
"""

import unittest
import bisect


class CountIntervals:
    """Disjoint interval set with running integer count."""

    def __init__(self) -> None:
        self.intervals: list[list[int]] = []
        self.total_count: int = 0

    def add(self, left: int, right: int) -> None:
        idx = bisect.bisect_left(self.intervals, [left, left])
        # Check if overlaps with previous interval
        if idx > 0 and self.intervals[idx - 1][1] >= left:
            idx -= 1

        new_left, new_right = left, right
        to_remove = 0

        while idx < len(self.intervals) and self.intervals[idx][0] <= right:
            cur_l, cur_r = self.intervals[idx]
            new_left = min(new_left, cur_l)
            new_right = max(new_right, cur_r)
            self.total_count -= cur_r - cur_l + 1
            self.intervals.pop(idx)

        self.intervals.insert(idx, [new_left, new_right])
        self.total_count += new_right - new_left + 1

    def count(self) -> int:
        return self.total_count
class TestCountIntervals(unittest.TestCase):
    def test_example_1(self) -> None:
        ci = CountIntervals()
        ci.add(2, 3)
        ci.add(7, 10)
        self.assertEqual(ci.count(), 6)
        ci.add(5, 8)
        self.assertEqual(ci.count(), 8)


if __name__ == "__main__":
    unittest.main()
