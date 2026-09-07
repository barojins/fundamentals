"""
LeetCode 1244: Design A Leaderboard
Difficulty: Medium
Tags: Hash Table, Design, Sorting, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a Leaderboard class, which has 3 functions:
1. `addScore(playerId, score)`: Update the leaderboard by adding `score` to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given `score`.
2. `top(K)`: Return the score sum of the top `K` players.
3. `reset(playerId)`: Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard).

Implement the `Leaderboard` class.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output:
[null,null,null,null,null,null,73,null,null,null,141]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addScore`, `reset`: O(1)
- `top(K)`: O(N log K) using min-heap of size K.
Space Complexity: O(P) where P is number of active players.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map `player_id -> score: dict[int, int]`.
- `addScore(playerId, score)`: `scores[playerId] += score`.
- `reset(playerId)`: `del scores[playerId]`.
- `top(K)`: `sum(heapq.nlargest(K, scores.values()))`.
"""

import unittest
import heapq


class Leaderboard:
    """Player leaderboard with top-K score aggregation."""

    def __init__(self) -> None:
        self.scores: dict[int, int] = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        top_k = heapq.nlargest(K, self.scores.values())
        return sum(top_k)

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]
class TestLeaderboard(unittest.TestCase):
    def test_example_1(self) -> None:
        lb = Leaderboard()
        lb.addScore(1, 73)
        lb.addScore(2, 56)
        lb.addScore(3, 39)
        lb.addScore(4, 51)
        lb.addScore(5, 4)
        self.assertEqual(lb.top(1), 73)
        lb.reset(1)
        lb.reset(2)
        lb.addScore(2, 51)
        self.assertEqual(lb.top(3), 141)


if __name__ == "__main__":
    unittest.main()
