"""
LeetCode 352: Data Stream as Disjoint Intervals
Difficulty: Hard
Tags: Binary Search, Design, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given a data stream input of non-negative integers `a_1, a_2, ..., a_n`, summarize the numbers seen so far as a list of disjoint intervals.

Implement the `SummaryRanges` class:
- `SummaryRanges()` Initializes the object with an empty stream.
- `void addNum(int value)` Adds the integer `value` to the stream.
- `int[][] getIntervals()` Returns a summary of the integers in the stream currently as a list of disjoint intervals `[start_i, end_i]`. The answer should be sorted by `start_i`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output:
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addNum(val)`: O(log N) using balanced BST or sorted list / bisect
- `getIntervals()`: O(N) to return intervals
Space Complexity: O(N) to store distinct intervals.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain a sorted set or sorted array of disjoint intervals `[start, end]`.
On `addNum(val)`:
- Binary search for position where interval starting after or containing `val` lies.
- Check merging conditions:
  1. Already inside an existing interval -> no-op.
  2. Merges with previous interval and next interval into one.
  3. Extends previous interval by 1 (`prev.end + 1 == val`).
  4. Extends next interval by 1 (`val + 1 == next.start`).
  5. Inserts as a new isolated interval `[val, val]`.
"""

import bisect
import unittest


class SummaryRanges:
    """Maintains disjoint intervals over streaming integers."""

    def __init__(self) -> None:
        self.intervals: list[list[int]] = []

    def addNum(self, value: int) -> None:
        idx = bisect.bisect_right(self.intervals, [value, float("inf")])

        # Check if value is covered by interval at idx - 1
        if idx > 0 and self.intervals[idx - 1][1] >= value:
            return

        left_merge = idx > 0 and self.intervals[idx - 1][1] + 1 == value
        right_merge = (
            idx < len(self.intervals) and self.intervals[idx][0] - 1 == value
        )

        if left_merge and right_merge:
            self.intervals[idx - 1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        elif left_merge:
            self.intervals[idx - 1][1] = value
        elif right_merge:
            self.intervals[idx][0] = value
        else:
            self.intervals.insert(idx, [value, value])

    def getIntervals(self) -> list[list[int]]:
        return self.intervals


class TestSummaryRanges(unittest.TestCase):
    def test_example_1(self) -> None:
        sr = SummaryRanges()
        sr.addNum(1)
        self.assertEqual(sr.getIntervals(), [[1, 1]])
        sr.addNum(3)
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 3]])
        sr.addNum(7)
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 3], [7, 7]])
        sr.addNum(2)
        self.assertEqual(sr.getIntervals(), [[1, 3], [7, 7]])
        sr.addNum(6)
        self.assertEqual(sr.getIntervals(), [[1, 3], [6, 7]])

    def test_duplicate_add(self) -> None:
        sr = SummaryRanges()
        sr.addNum(1)
        sr.addNum(1)
        sr.addNum(1)
        self.assertEqual(sr.getIntervals(), [[1, 1]])

    def test_merge_all(self) -> None:
        sr = SummaryRanges()
        sr.addNum(1)
        sr.addNum(3)
        sr.addNum(2)
        self.assertEqual(sr.getIntervals(), [[1, 3]])


if __name__ == "__main__":
    unittest.main()
