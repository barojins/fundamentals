"""
LeetCode 2080: Range Frequency Queries
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Design, Segment Tree

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure to find the frequency of a given value in a given subarray.

Implement the `RangeFreqQuery` class:
- `RangeFreqQuery(int[] arr)` Constructs an instance of the class with the given integer array `arr`.
- `int query(int left, int right, int value)` Returns the frequency of `value` in the subarray `arr[left...right]`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
Output:
[null, 1, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N)
- `query`: O(log K) using binary search `bisect` over matching indices.
Space Complexity: O(N) for indices map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store sorted index lists for each value in `val_to_indices: dict[int, list[int]]`.
For `query(left, right, value)`:
`bisect_right(indices, right) - bisect_left(indices, left)`.
"""

import unittest
from collections import defaultdict
import bisect


class RangeFreqQuery:
    """Subarray value frequency queries using binary search on index lists."""

    def __init__(self, arr: list[int]) -> None:
        self.indices: dict[int, list[int]] = defaultdict(list)
        for i, val in enumerate(arr):
            self.indices[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.indices:
            return 0
        locs = self.indices[value]
        r = bisect.bisect_right(locs, right)
        l = bisect.bisect_left(locs, left)
        return r - l
class TestRangeFreqQuery(unittest.TestCase):
    def test_example_1(self) -> None:
        rfq = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
        self.assertEqual(rfq.query(1, 2, 4), 1)
        self.assertEqual(rfq.query(0, 11, 33), 2)


if __name__ == "__main__":
    unittest.main()
