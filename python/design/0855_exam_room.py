"""
LeetCode 855: Exam Room
Difficulty: Medium
Tags: Design, Heap (Priority Queue), Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
There is an exam room with `n` seats in a single row labeled from `0` to `n - 1`.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number `0`.

Design a class that simulates the seating and leaving of students.

Implement the `ExamRoom` class:
- `ExamRoom(int n)` Initializes the object of the exam room with the number of the seats `n`.
- `int seat()` Returns the label of the seat at which the next student will sit.
- `void leave(int p)` Indicates that the student sitting at seat `p` will leave the room. It is guaranteed that there will be a student sitting at seat `p`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]
Output:
[null, 0, 9, 4, 2, null, 5]

Explanation:
ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
examRoom.seat(); // return 9, the student sits at the last seat number 9.
examRoom.seat(); // return 4, the student sits at the seat number 4.
examRoom.seat(); // return 2, the student sits at the seat number 2.
examRoom.leave(4);
examRoom.seat(); // return 5, the student sits at the seat number 5.

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `seat()`: O(N) where N is number of seated students.
- `leave(p)`: O(N) to remove from sorted list.
Space Complexity: O(N) to store occupied seats in order.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain a sorted list of seated student positions `self.seats: list[int]`.
When seating:
- If empty, return `0`.
- Check edge distance at seat `0` (`dist = seats[0]`).
- For each adjacent pair `(seats[i], seats[i+1])`, midpoint is `(seats[i] + seats[i+1]) // 2` with distance `(seats[i+1] - seats[i]) // 2`.
- Check edge distance at seat `n - 1` (`dist = (n - 1) - seats[-1]`).
Pick candidate seat that strictly maximizes distance (and tie-breaks with lowest index).
Insert into sorted list.
"""

import unittest
import bisect


class ExamRoom:
    """Maximizes distance to nearest person in a row of n seats."""

    def __init__(self, n: int) -> None:
        self.n: int = n
        self.seats: list[int] = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0

        # Check left edge (seat 0)
        max_dist = self.seats[0]
        chosen_seat = 0

        # Check all internal intervals
        for i in range(len(self.seats) - 1):
            prev_seat, next_seat = self.seats[i], self.seats[i + 1]
            dist = (next_seat - prev_seat) // 2
            if dist > max_dist:
                max_dist = dist
                chosen_seat = prev_seat + dist

        # Check right edge (seat n - 1)
        right_dist = (self.n - 1) - self.seats[-1]
        if right_dist > max_dist:
            chosen_seat = self.n - 1

        bisect.insort(self.seats, chosen_seat)
        return chosen_seat

    def leave(self, p: int) -> None:
        self.seats.remove(p)
class TestExamRoom(unittest.TestCase):
    def test_example_1(self) -> None:
        room = ExamRoom(10)
        self.assertEqual(room.seat(), 0)
        self.assertEqual(room.seat(), 9)
        self.assertEqual(room.seat(), 4)
        self.assertEqual(room.seat(), 2)
        room.leave(4)
        self.assertEqual(room.seat(), 5)


if __name__ == "__main__":
    unittest.main()
