"""
LeetCode 1756: Design Most Recently Used Queue
Difficulty: Medium
Tags: Array, Design, Binary Indexed Tree, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a queue-like data structure that moves the most recently used element to the end of the queue.

Implement the `MRUQueue` class:
- `MRUQueue(int n)` constructs the `MRUQueue` with `n` elements: `[1, 2, ..., n]`.
- `int fetch(int k)` moves the `k-th` element (1-indexed) to the end of the queue and returns it.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
Output:
[null, 3, 6, 2, 2]

Explanation:
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // Moves the 8th element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `fetch`: O(sqrt(N)) using Sqrt Decomposition (or O(log N) with Fenwick Tree / Treap).
Space Complexity: O(N) to store elements.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use Square Root Decomposition:
Partition the elements into `sqrt(N)` buckets of length ~`sqrt(N)`.
To `fetch(k)`:
- Locate the target bucket containing the `k`-th element.
- Pop the element from that bucket.
- Append it to the last bucket.
- Rebalance buckets (shift the head of each subsequent bucket to the tail of the preceding bucket) in O(sqrt(N)) time.
"""

import unittest
import math


class MRUQueue:
    """Most Recently Used Queue using Sqrt-Decomposition for O(sqrt N) fetch."""

    def __init__(self, n: int) -> None:
        self.B: int = max(1, int(math.isqrt(n)))
        self.buckets: list[list[int]] = []
        for i in range(1, n + 1, self.B):
            self.buckets.append(list(range(i, min(i + self.B, n + 1))))

    def fetch(self, k: int) -> int:
        idx = k - 1  # 0-indexed

        # Find target bucket
        bucket_idx = 0
        while idx >= len(self.buckets[bucket_idx]):
            idx -= len(self.buckets[bucket_idx])
            bucket_idx += 1

        val = self.buckets[bucket_idx].pop(idx)
        self.buckets[-1].append(val)

        # Shift one element back for each bucket between bucket_idx and end
        for b in range(bucket_idx, len(self.buckets) - 1):
            shifted = self.buckets[b + 1].pop(0)
            self.buckets[b].append(shifted)

        return val
class TestMRUQueue(unittest.TestCase):
    def test_example_1(self) -> None:
        mru = MRUQueue(8)
        self.assertEqual(mru.fetch(3), 3)
        self.assertEqual(mru.fetch(5), 6)
        self.assertEqual(mru.fetch(2), 2)
        self.assertEqual(mru.fetch(8), 2)


if __name__ == "__main__":
    unittest.main()
