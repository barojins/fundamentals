"""
LeetCode 2102: Sequentially Ordinal Rank Tracker
Difficulty: Hard
Tags: Design, Heap (Priority Queue), Ordered Set, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A scenic location tracking system tracks locations by their scores. If two locations have the same score, the one with the lexicographically smaller name is ranked higher.

Implement the `SORTracker` class:
- `SORTracker()` Initializes the tracker system.
- `void add(string name, int score)` Adds a scenic location with name `name` and score `score` to the system.
- `string get()` Queries and returns the `i-th` best location, where `i` is the number of times this method has been invoked (1-indexed).

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
Output:
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add`: O(log N)
- `get`: O(log N)
Space Complexity: O(N) using two balanced heaps.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain two heaps partitioned around the `k`-th best element:
- `left` (min-heap of size `k` tracking top elements): `(score, -name)`
- `right` (max-heap tracking remaining elements): `(-score, name)`
On `add(name, score)`: push to `left`, balance to `right`.
On `get()`: shift top of `right` to `left`, and return top of `left`.
"""

import unittest
import heapq


class LocationLeft:
    """Wrapper for left heap: min-heap comparing (score, -name)."""

    def __init__(self, score: int, name: str) -> None:
        self.score: int = score
        self.name: str = name

    def __lt__(self, other: "LocationLeft") -> bool:
        if self.score != other.score:
            return self.score < other.score
        return self.name > other.name


class LocationRight:
    """Wrapper for right heap: min-heap comparing (-score, name)."""

    def __init__(self, score: int, name: str) -> None:
        self.score: int = score
        self.name: str = name

    def __lt__(self, other: "LocationRight") -> bool:
        if self.score != other.score:
            return self.score > other.score
        return self.name < other.name


class SORTracker:
    """Sequentially Ordinal Rank Tracker using dual balanced heaps."""

    def __init__(self) -> None:
        self.left: list[LocationLeft] = []
        self.right: list[LocationRight] = []
        self.k: int = 0

    def add(self, name: str, score: int) -> None:
        loc_l = LocationLeft(score, name)
        heapq.heappush(self.left, loc_l)
        # Rebalance: move smallest of top-k to right heap
        popped = heapq.heappop(self.left)
        heapq.heappush(self.right, LocationRight(popped.score, popped.name))

    def get(self) -> str:
        self.k += 1
        # Pull best from right into left
        best = heapq.heappop(self.right)
        heapq.heappush(self.left, LocationLeft(best.score, best.name))
        return self.left[0].name
class TestSORTracker(unittest.TestCase):
    def test_example_1(self) -> None:
        tracker = SORTracker()
        tracker.add("bradford", 2)
        tracker.add("branford", 3)
        self.assertEqual(tracker.get(), "branford")
        tracker.add("alps", 2)
        self.assertEqual(tracker.get(), "alps")
        tracker.add("orland", 2)
        self.assertEqual(tracker.get(), "bradford")
        tracker.add("orlando", 3)
        self.assertEqual(tracker.get(), "bradford")
        tracker.add("alpine", 2)
        self.assertEqual(tracker.get(), "bradford")
        self.assertEqual(tracker.get(), "orland")


if __name__ == "__main__":
    unittest.main()
