"""
LeetCode 911: Online Election
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given two integer arrays `persons` and `times`. In an election, the `i-th` vote was cast for `persons[i]` at time `times[i]`.

For each query at a time `t`, find the person that was leading the election at time `t`. Votes cast at time `t` will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the `TopVotedCandidate` class:
- `TopVotedCandidate(int[] persons, int[] times)` Initializes the object with the `persons` and `times` arrays.
- `int q(int t)` Returns the number of the person that was leading the election at time `t` according to the mentioned rules.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
Output:
[null, 0, 1, 1, 0, 0, 1]

Explanation:
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3);  // return 0, At time 3, the votes are [0], and 0 is leading.
topVotedCandidate.q(12); // return 1, At time 12, the votes are [0,1,1], and 1 is leading.
topVotedCandidate.q(25); // return 1, At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (tie broken by most recent vote).
topVotedCandidate.q(15); // return 0
topVotedCandidate.q(24); // return 0
topVotedCandidate.q(8);  // return 1

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N) where N is number of votes.
- `q(t)`: O(log N) using binary search `bisect_right`.
Space Complexity: O(N) to store leaders at each timestamp.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Precompute the leader at each vote timestamp during `__init__`.
Track vote counts in a `Counter` and maintain the current leader:
When a candidate's vote count reaches `>= max_votes`, they become the new leader (handling ties because of `>=`).
On query `q(t)`: binary search `bisect_right` on `times` to find the leader at that point in time.
"""

import unittest
from collections import Counter
import bisect


class TopVotedCandidate:
    """Precomputed election leaders with binary search lookup at any timestamp."""

    def __init__(self, persons: list[int], times: list[int]) -> None:
        self.times: list[int] = times
        self.leaders: list[int] = []
        counts: Counter[int] = Counter()
        curr_leader: int = -1
        max_votes: int = 0

        for p in persons:
            counts[p] += 1
            if counts[p] >= max_votes:
                curr_leader = p
                max_votes = counts[p]
            self.leaders.append(curr_leader)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]
class TestTopVotedCandidate(unittest.TestCase):
    def test_example_1(self) -> None:
        tvc = TopVotedCandidate(
        [0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]
        )
        self.assertEqual(tvc.q(3), 0)
        self.assertEqual(tvc.q(12), 1)
        self.assertEqual(tvc.q(25), 1)
        self.assertEqual(tvc.q(15), 0)
        self.assertEqual(tvc.q(24), 0)
        self.assertEqual(tvc.q(8), 1)


if __name__ == "__main__":
    unittest.main()
