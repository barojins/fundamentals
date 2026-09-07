"""
LeetCode 1845: Seat Reservation Manager
Difficulty: Medium
Tags: Design, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a system that manages the reservation state of `n` seats that are numbered from `1` to `n`.

Implement the `SeatManager` class:
- `SeatManager(int n)` Initializes a `SeatManager` object that will manage `n` seats numbered from `1` to `n`. All seats are initially available.
- `int reserve()` Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
- `void unreserve(int seatNumber)` Unreserves the seat with the given `seatNumber`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output:
[null, 1, 2, null, 2, 3, 4, 5, null]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `reserve`: O(log N)
- `unreserve`: O(log N)
Space Complexity: O(N) for min-heap.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a min-heap:
Initialize heap with numbers `1` to `n` (or keep a high-water mark pointer + unreserved min-heap).
- `reserve()`: `heapq.heappop(self.available)`
- `unreserve(seatNumber)`: `heapq.heappush(self.available, seatNumber)`.
"""

import unittest
import heapq


class SeatManager:
    """Seat reservation manager using a min-heap."""

    def __init__(self, n: int) -> None:
        self.available: list[int] = list(range(1, n + 1))
        heapq.heapify(self.available)

    def reserve(self) -> int:
        return heapq.heappop(self.available)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)
class TestSeatManager(unittest.TestCase):
    def test_example_1(self) -> None:
        sm = SeatManager(5)
        self.assertEqual(sm.reserve(), 1)
        self.assertEqual(sm.reserve(), 2)
        sm.unreserve(2)
        self.assertEqual(sm.reserve(), 2)
        self.assertEqual(sm.reserve(), 3)
        self.assertEqual(sm.reserve(), 4)
        self.assertEqual(sm.reserve(), 5)
        sm.unreserve(5)


if __name__ == "__main__":
    unittest.main()
