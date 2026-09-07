"""
LeetCode 933: Number of Recent Calls
Difficulty: Easy
Tags: Design, Queue, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:
- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that have happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a strictly larger value of `t` than the previous call.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output:
[null, 1, 2, 3, 3]

Explanation:
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3 (1 is evicted)

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `ping(t)`: O(1) amortized
Space Complexity: O(W) where W is maximum number of requests in 3000ms window.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a `collections.deque` of timestamps:
On `ping(t)`:
- Append `t` to queue.
- Pop timestamps from left while `queue[0] < t - 3000`.
- Return `len(queue)`.
"""

import unittest
from collections import deque


class RecentCounter:
    """Sliding-window request rate counter over 3000 ms."""

    def __init__(self) -> None:
        self.queue: deque[int] = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
class TestRecentCounter(unittest.TestCase):
    def test_example_1(self) -> None:
        rc = RecentCounter()
        self.assertEqual(rc.ping(1), 1)
        self.assertEqual(rc.ping(100), 2)
        self.assertEqual(rc.ping(3001), 3)
        self.assertEqual(rc.ping(3002), 3)


if __name__ == "__main__":
    unittest.main()
