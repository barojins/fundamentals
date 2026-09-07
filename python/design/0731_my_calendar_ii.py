"""
LeetCode 731: My Calendar II
Difficulty: Medium
Tags: Array, Binary Search, Design, Segment Tree, Ordered Set, Prefix Sum

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection.

Implement the `MyCalendarTwo` class:
- `MyCalendarTwo()` Initializes the calendar object.
- `boolean book(int startTime, int endTime)` Returns `true` if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return `false`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output:
[null, true, true, true, false, true, true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `book`: O(N) where N is number of booked events.
Space Complexity: O(N) to store bookings and double bookings.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain two lists of intervals:
- `self.overlaps`: Intervals with existing double bookings.
- `self.bookings`: All booked single intervals.
When booking `[start, end)`:
1. First check against `self.overlaps`. If any overlap exists, booking fails (would cause triple booking).
2. Otherwise, find intersections with all intervals in `self.bookings` and add those intersections to `self.overlaps`. Add `[start, end)` to `self.bookings`.
"""

import unittest
class MyCalendarTwo:
    """Calendar allowing at most double bookings (rejects triple bookings)."""

    def __init__(self) -> None:
        self.bookings: list[tuple[int, int]] = []
        self.overlaps: list[tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Check if booking overlaps with any already double-booked interval
        for o_start, o_end in self.overlaps:
            if max(startTime, o_start) < min(endTime, o_end):
                return False

        # Add new double-booking overlaps
        for b_start, b_end in self.bookings:
            inter_start = max(startTime, b_start)
            inter_end = min(endTime, b_end)
            if inter_start < inter_end:
                self.overlaps.append((inter_start, inter_end))

        self.bookings.append((startTime, endTime))
        return True
class TestMyCalendarTwo(unittest.TestCase):
    def test_example_1(self) -> None:
        cal2 = MyCalendarTwo()
        self.assertTrue(cal2.book(10, 20))
        self.assertTrue(cal2.book(50, 60))
        self.assertTrue(cal2.book(10, 40))
        self.assertFalse(cal2.book(5, 15))
        self.assertTrue(cal2.book(5, 10))
        self.assertTrue(cal2.book(25, 55))


if __name__ == "__main__":
    unittest.main()
