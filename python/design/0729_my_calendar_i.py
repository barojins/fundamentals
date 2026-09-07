"""
LeetCode 729: My Calendar I
Difficulty: Medium
Tags: Array, Binary Search, Design, Segment Tree, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events).

The event can be represented as a pair of integers `startTime` and `endTime` that represents a booking on the half-open interval `[startTime, endTime)`.

Implement the `MyCalendar` class:
- `MyCalendar()` Initializes the calendar object.
- `boolean book(int startTime, int endTime)` Returns `true` if the event can be added to the calendar successfully without causing a double booking. Otherwise, return `false`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output:
[null, true, false, true]

Explanation:
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `book`: O(log N) with binary search / balanced BST (or O(N) array insertion).
Space Complexity: O(N) for stored booked intervals.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain sorted intervals `[start, end]`.
Using binary search `bisect_right`:
Find the interval immediately before and after `[startTime, endTime)`.
Conflict occurs if `prev_interval.end > startTime` or `next_interval.start < endTime`.
"""

import unittest
import bisect


class MyCalendar:
    """Non-overlapping calendar booking using binary search on sorted intervals."""

    def __init__(self) -> None:
        self.bookings: list[tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect.bisect_right(self.bookings, (startTime, endTime))

        if idx > 0 and self.bookings[idx - 1][1] > startTime:
            return False
        if idx < len(self.bookings) and self.bookings[idx][0] < endTime:
            return False

        self.bookings.insert(idx, (startTime, endTime))
        return True
class TestMyCalendar(unittest.TestCase):
    def test_example_1(self) -> None:
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(15, 25))
        self.assertTrue(cal.book(20, 30))


if __name__ == "__main__":
    unittest.main()
