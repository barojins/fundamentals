"""
LeetCode 362: Design Hit Counter
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Design, Queue, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a hit counter which counts the number of hits received in the past `5` minutes (i.e., the past `300` seconds).

Your system should accept a `timestamp` parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., `timestamp` is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the `HitCounter` class:
- `HitCounter()` Initializes the object of the hit counter system.
- `void hit(int timestamp)` Records a hit that happened at `timestamp` (in seconds). Several hits may happen at the same `timestamp`.
- `int getHits(int timestamp)` Returns the number of hits in the past 5 minutes from `timestamp` (i.e., the past 300 seconds).

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]
Output:
[null, null, null, null, 3, null, 4, 3]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `hit(timestamp)`: O(1)
- `getHits(timestamp)`: O(1) (circular buffer of 300 buckets)
Space Complexity: O(1) fixed 300 buckets.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use two fixed-size arrays of size 300: `times = [0] * 300` and `hits = [0] * 300`.
For timestamp `t`:
- `idx = t % 300`
- If `times[idx] != t`, reset `times[idx] = t` and `hits[idx] = 1`.
- Otherwise increment `hits[idx] += 1`.
For `getHits(t)`:
- Sum all `hits[i]` where `t - times[i] < 300`.
"""

import unittest


class HitCounter:
    """Fixed-bucket O(1) Hit Counter for a 300-second window."""

    def __init__(self) -> None:
        self.times: list[int] = [0] * 300
        self.hits: list[int] = [0] * 300

    def hit(self, timestamp: int) -> None:
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total


class TestHitCounter(unittest.TestCase):
    def test_example_1(self) -> None:
        counter = HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.getHits(4), 3)
        counter.hit(300)
        self.assertEqual(counter.getHits(300), 4)
        self.assertEqual(counter.getHits(301), 3)

    def test_multiple_hits_same_timestamp(self) -> None:
        counter = HitCounter()
        counter.hit(1)
        counter.hit(1)
        counter.hit(1)
        self.assertEqual(counter.getHits(1), 3)
        self.assertEqual(counter.getHits(300), 3)
        self.assertEqual(counter.getHits(301), 0)


if __name__ == "__main__":
    unittest.main()
