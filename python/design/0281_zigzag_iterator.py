"""
LeetCode 281: Zigzag Iterator
Difficulty: Medium
Tags: Array, Design, Queue, Iterator

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given two 1D vectors, implement an iterator to return their elements alternately.

Implement the `ZigzagIterator` class:
- `ZigzagIterator(List<Integer> v1, List<Integer> v2)`
- `boolean hasNext()`
- `int next()`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next`, `hasNext`: O(1)
Space Complexity: O(K) for active vector queue.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store active `(vector, index)` in a queue, popping from front and re-enqueueing if index + 1 < len.
"""

import unittest
from collections import deque


class ZigzagIterator:
    """Interleaves elements from 1D vectors in round-robin order."""

    def __init__(self, v1: list[int], v2: list[int]) -> None:
        self.queue: deque[tuple[list[int], int]] = deque()
        for v in [v1, v2]:
            if v:
                self.queue.append((v, 0))

    def next(self) -> int:
        vec, idx = self.queue.popleft()
        val = vec[idx]
        if idx + 1 < len(vec):
            self.queue.append((vec, idx + 1))
        return val

    def hasNext(self) -> bool:
        return len(self.queue) > 0


class TestZigzagIterator(unittest.TestCase):
    def test_example_1(self) -> None:
        zit = ZigzagIterator([1, 2], [3, 4, 5, 6])
        out = []
        while zit.hasNext():
            out.append(zit.next())
        self.assertEqual(out, [1, 3, 2, 4, 5, 6])

    def test_one_empty(self) -> None:
        zit = ZigzagIterator([], [1, 2, 3])
        out = []
        while zit.hasNext():
            out.append(zit.next())
        self.assertEqual(out, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
