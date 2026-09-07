"""
LeetCode 353: Design Snake Game
Difficulty: Medium
Tags: Array, Hash Table, Design, Queue, Matrix, Simulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a Snake game that is played on a device with screen size `height x width`.
The snake is initially positioned at the top left corner `(0, 0)` with a length of `1` unit.

You are given an array `food` where `food[i] = (r_i, c_i)` is the row and column of the next food piece that will appear on the screen.
When the snake eats a food piece, its length increases by `1` and the next food piece appears at the specified position.
The game is over if a snake goes out of bounds (hits a wall) or if its head hits its own body.

Implement the `SnakeGame` class:
- `SnakeGame(int width, int height, int[][] food)` Initializes the object with a screen of size `height x width` and the positions of the `food`.
- `int move(String direction)` Returns the score of the game after applying one `direction` move ('U', 'D', 'L', 'R'). If the game is over, return `-1`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["SnakeGame", "move", "move", "move", "move", "move", "move"]
[[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
Output:
[null, 0, 0, 1, 1, 2, -1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `move(direction)`: O(1)
Space Complexity: O(N + F) where N is width * height and F is food count.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a deque `body` storing `(r, c)` tuples and a set `body_set` for O(1) collision detection.
On `move(direction)`:
1. Compute new head coordinate `(nr, nc)`.
2. Check wall collision: `0 <= nr < height` and `0 <= nc < width`.
3. Check food: if food remains and `(nr, nc) == food[food_idx]`, consume food, advance `food_idx`, score increases by 1.
4. If no food, pop tail from deque and remove from `body_set`.
5. Check body collision: if `(nr, nc) in body_set`, return -1.
6. Append new head to `body` and `body_set`. Return current score.
"""

from collections import deque
import unittest


class SnakeGame:
    """Snake game simulation on a grid with food sequence."""

    def __init__(self, width: int, height: int, food: list[list[int]]) -> None:
        self.width: int = width
        self.height: int = height
        self.food: list[list[int]] = food
        self.food_idx: int = 0
        self.score: int = 0
        self.body: deque[tuple[int, int]] = deque([(0, 0)])
        self.body_set: set[tuple[int, int]] = {(0, 0)}
        self.dirs: dict[str, tuple[int, int]] = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
        }

    def move(self, direction: str) -> int:
        dr, dc = self.dirs[direction]
        head_r, head_c = self.body[0]
        nr, nc = head_r + dr, head_c + dc

        # Wall collision
        if not (0 <= nr < self.height and 0 <= nc < self.width):
            return -1

        # Check food
        if self.food_idx < len(self.food) and [nr, nc] == self.food[self.food_idx]:
            self.food_idx += 1
            self.score += 1
        else:
            tail = self.body.pop()
            self.body_set.remove(tail)

        # Body collision (after removing tail if not grown)
        if (nr, nc) in self.body_set:
            return -1

        self.body.appendleft((nr, nc))
        self.body_set.add((nr, nc))
        return self.score


class TestSnakeGame(unittest.TestCase):
    def test_example_1(self) -> None:
        game = SnakeGame(3, 2, [[1, 2], [0, 1]])
        self.assertEqual(game.move("R"), 0)
        self.assertEqual(game.move("D"), 0)
        self.assertEqual(game.move("R"), 1)
        self.assertEqual(game.move("U"), 1)
        self.assertEqual(game.move("L"), 2)
        self.assertEqual(game.move("U"), -1)

    def test_immediate_wall_crash(self) -> None:
        game = SnakeGame(2, 2, [])
        self.assertEqual(game.move("U"), -1)

    def test_tail_chase_no_crash(self) -> None:
        # Snake of length 3 chasing its own tail in a 2x2 loop
        game = SnakeGame(2, 2, [[0, 1], [1, 1], [1, 0]])
        self.assertEqual(game.move("R"), 1)  # (0,1)
        self.assertEqual(game.move("D"), 2)  # (1,1)
        self.assertEqual(game.move("L"), 3)  # (1,0)
        # moving U to (0,0) which was the tail - should succeed because tail moves away
        self.assertEqual(game.move("U"), 3)


if __name__ == "__main__":
    unittest.main()
