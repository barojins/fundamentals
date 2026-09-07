"""
LeetCode 2069: Walking Robot Simulation II
Difficulty: Medium
Tags: Design, Simulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A `width x height` grid is on an X-Y plane with the bottom-left cell at `(0, 0)` and the top-right cell at `(width - 1, height - 1)`. The grid is aligned with the four cardinal directions ("East", "North", "West", and "South").

A robot is initially at `(0, 0)` facing `"East"`.

Implement the `Robot` class:
- `Robot(int width, int height)` Initializes the grid and the robot.
- `void step(int num)` Moves the robot `num` steps forward along the perimeter counterclockwise.
- `int[] getPos()` Returns the current position of the robot `[x, y]`.
- `String getDir()` Returns the current direction of the robot.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output:
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `step`: O(1) modulo perimeter
- `getPos`, `getDir`: O(1)
Space Complexity: O(1)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
The robot only ever walks the outer perimeter of length `perimeter = 2 * (width + height - 2)`.
Maintain 1D perimeter offset `self.pos = (self.pos + num) % perimeter`.
Special case: if robot is at `(0, 0)` after moving at least once, its direction is `"South"`, not `"East"`.
"""

import unittest
class Robot:
    """Perimeter-walking robot with O(1) step execution."""

    def __init__(self, width: int, height: int) -> None:
        self.w: int = width
        self.h: int = height
        self.perimeter: int = 2 * (width + height - 2)
        self.pos: int = 0
        self.has_moved: bool = False

    def step(self, num: int) -> None:
        self.has_moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        p = self.pos
        if p <= self.w - 1:
            return [p, 0]
        p -= self.w - 1
        if p <= self.h - 1:
            return [self.w - 1, p]
        p -= self.h - 1
        if p <= self.w - 1:
            return [self.w - 1 - p, self.h - 1]
        p -= self.w - 1
        return [0, self.h - 1 - p]

    def getDir(self) -> str:
        if not self.has_moved:
            return "East"

        p = self.pos
        if p == 0:
            return "South"
        elif 1 <= p <= self.w - 1:
            return "East"
        elif self.w <= p <= self.w + self.h - 2:
            return "North"
        elif self.w + self.h - 1 <= p <= 2 * self.w + self.h - 3:
            return "West"
        else:
            return "South"
class TestRobot(unittest.TestCase):
    def test_example_1(self) -> None:
        robot = Robot(6, 3)
        robot.step(2)
        robot.step(2)
        self.assertEqual(robot.getPos(), [4, 0])
        self.assertEqual(robot.getDir(), "East")
        robot.step(2)
        robot.step(1)
        robot.step(4)
        self.assertEqual(robot.getPos(), [1, 2])
        self.assertEqual(robot.getDir(), "West")


if __name__ == "__main__":
    unittest.main()
