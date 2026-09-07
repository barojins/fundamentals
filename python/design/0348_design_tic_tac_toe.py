"""
LeetCode 348: Design Tic-Tac-Toe
Difficulty: Medium
Tags: Array, Hash Table, Design, Matrix, Simulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Assume the following rules are for the tic-tac-toe game on an `n x n` board between two players:
1. A move is guaranteed to be valid and is placed on an empty block.
2. The first player to place `n` of their marks in a horizontal, vertical, or diagonal row wins the game.
3. Once a winning condition is reached, no more moves will be made.

Implement the `TicTacToe` class:
- `TicTacToe(int n)` Initializes the object the size of the board `n`.
- `int move(int row, int col, int player)` Indicates that the player with id `player` plays at the cell `(row, col)`. The move is guaranteed to be a valid move. Returns:
  - `0` if no one wins after the move.
  - `1` if player 1 wins.
  - `2` if player 2 wins.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output:
[null, 0, 0, 0, 0, 0, 0, 1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `move`: O(1)
Space Complexity: O(n) for row/col/diagonal tallies.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Instead of storing the full n x n board, track scores for each row, col, main diagonal, and anti-diagonal.
Represent player 1 as `+1` and player 2 as `-1`.
When a move is made at `(row, col)`:
- `rows[row] += val`
- `cols[col] += val`
- If `row == col`: `diagonal += val`
- If `row + col == n - 1`: `anti_diagonal += val`
If any absolute tally reaches `n`, the current player wins!
"""

import unittest


class TicTacToe:
    """O(1) per-move Tic-Tac-Toe game engine."""

    def __init__(self, n: int) -> None:
        self.n: int = n
        self.rows: list[int] = [0] * n
        self.cols: list[int] = [0] * n
        self.diag: int = 0
        self.anti_diag: int = 0

    def move(self, row: int, col: int, player: int) -> int:
        delta = 1 if player == 1 else -1

        self.rows[row] += delta
        self.cols[col] += delta

        if row == col:
            self.diag += delta
        if row + col == self.n - 1:
            self.anti_diag += delta

        if (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.diag) == self.n
            or abs(self.anti_diag) == self.n
        ):
            return player

        return 0

class TestTicTacToe(unittest.TestCase):
    def test_example_1(self) -> None:
        game = TicTacToe(3)
        self.assertEqual(game.move(0, 0, 1), 0)
        self.assertEqual(game.move(0, 2, 2), 0)
        self.assertEqual(game.move(2, 2, 1), 0)
        self.assertEqual(game.move(1, 1, 2), 0)
        self.assertEqual(game.move(2, 0, 1), 0)
        self.assertEqual(game.move(1, 0, 2), 0)
        self.assertEqual(game.move(2, 1, 1), 1)

    def test_player2_wins(self) -> None:
        game = TicTacToe(3)
        self.assertEqual(game.move(0, 0, 1), 0)
        self.assertEqual(game.move(0, 1, 2), 0)
        self.assertEqual(game.move(1, 0, 1), 0)
        self.assertEqual(game.move(1, 1, 2), 0)
        self.assertEqual(game.move(2, 2, 1), 0)
        self.assertEqual(game.move(2, 1, 2), 2)

    def test_anti_diagonal_win(self) -> None:
        game = TicTacToe(3)
        self.assertEqual(game.move(0, 2, 1), 0)
        self.assertEqual(game.move(0, 0, 2), 0)
        self.assertEqual(game.move(1, 1, 1), 0)
        self.assertEqual(game.move(0, 1, 2), 0)
        self.assertEqual(game.move(2, 0, 1), 1)


if __name__ == "__main__":
    unittest.main()
