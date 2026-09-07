"""
LeetCode 1157: Online Majority Element In Subarray
Difficulty: Hard
Tags: Array, Binary Search, Design, Binary Indexed Tree, Segment Tree

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that efficiently finds the majority element of a given subarray.

The majority element of a subarray is an element that occurs `threshold` times or more in the subarray.

Implement the `MajorityChecker` class:
- `MajorityChecker(int[] arr)` Initializes the instance of the class with the given integer array `arr`.
- `int query(int left, int right, int threshold)` returns the element in `arr[left...right]` that occurs at least `threshold` times, or `-1` if no such element exists.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output:
[null, 1, -1, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N)
- `query`: O(T log N) randomized Boyer-Moore sampling / segment tree queries.
Space Complexity: O(N) for indices map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map each value to a list of its indices: `val_to_indices: dict[int, list[int]]`.
To count occurrences of `v` in `[left, right]`:
`bisect_right(locs, right) - bisect_left(locs, left)`.
To find majority candidates quickly:
Sample random elements from `arr[left...right]` up to 20-30 times. If an element has frequency >= threshold, it is guaranteed to be picked with probability >= 1 - (1 - threshold/len)^k.
"""

import unittest
from collections import defaultdict
import bisect
import random


class MajorityChecker:
    """Finds subarray majority element using index binary search + randomized sampling."""

    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.val_to_indices: dict[int, list[int]] = defaultdict(list)
        for i, val in enumerate(arr):
            self.val_to_indices[val].append(i)

    def _count_in_range(self, val: int, left: int, right: int) -> int:
        locs = self.val_to_indices[val]
        r_idx = bisect.bisect_right(locs, right)
        l_idx = bisect.bisect_left(locs, left)
        return r_idx - l_idx

    def query(self, left: int, right: int, threshold: int) -> int:
        # Sample random indices from [left, right]
        for _ in range(25):
            idx = random.randint(left, right)
            candidate = self.arr[idx]
            if self._count_in_range(candidate, left, right) >= threshold:
                return candidate
        return -1
class TestMajorityChecker(unittest.TestCase):
    def test_example_1(self) -> None:
        mc = MajorityChecker([1, 1, 2, 2, 1, 1])
        self.assertEqual(mc.query(0, 5, 4), 1)
        self.assertEqual(mc.query(0, 3, 3), -1)
        self.assertEqual(mc.query(2, 3, 2), 2)


if __name__ == "__main__":
    unittest.main()
