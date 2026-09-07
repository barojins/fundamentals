"""
LeetCode 732: My Calendar III
Difficulty: Hard
Tags: Binary Search, Design, Segment Tree, Ordered Set, Prefix Sum

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A `k`-booking happens when `k` events have some non-empty intersection.

Implement the `MyCalendarThree` class:
- `MyCalendarThree()` Initializes the object.
- `int book(int startTime, int endTime)` Returns an integer `k` representing the largest integer such that there exists a `k`-booking in the calendar.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output:
[null, 1, 1, 2, 3, 3, 3]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `book`: O(N log N) using boundary counting (or O(log C) with dynamic segment tree).
Space Complexity: O(N) to store time deltas.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use Sweep-Line / Boundary Counting with `collections.defaultdict(int)`:
- `timeline[startTime] += 1`
- `timeline[endTime] -= 1`
Iterate through sorted timestamps, accumulating running active bookings `curr_active += delta`, and tracking `max_k = max(max_k, curr_active)`.
"""

import unittest
from collections import defaultdict


class MyCalendarThree:
    """Computes maximum concurrent k-bookings using sweep-line boundary counting."""

    def __init__(self) -> None:
        self.timeline: dict[int, int] = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] += 1
        self.timeline[endTime] -= 1

        curr_active = 0
        max_k = 0
        for t in sorted(self.timeline.keys()):
            curr_active += self.timeline[t]
            max_k = max(max_k, curr_active)

        return max_k
class TestMyCalendarThree(unittest.TestCase):
    def test_example_1(self) -> None:
        cal3 = MyCalendarThree()
        self.assertEqual(cal3.book(10, 20), 1)
        self.assertEqual(cal3.book(50, 60), 1)
        self.assertEqual(cal3.book(10, 40), 2)
        self.assertEqual(cal3.book(5, 15), 3)
        self.assertEqual(cal3.book(5, 10), 3)
        self.assertEqual(cal3.book(25, 55), 3)


if __name__ == "__main__":
    unittest.main()
