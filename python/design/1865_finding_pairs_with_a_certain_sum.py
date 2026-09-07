"""
LeetCode 1865: Finding Pairs With a Certain Sum
Difficulty: Medium
Tags: Array, Hash Table, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a data structure that supports queries of two types:
1. Add a positive integer to an element of a given index in the array `nums2`.
2. Count the number of pairs `(i, j)` such that `nums1[i] + nums2[j]` equals a given value (`0 <= i < nums1.length` and `0 <= j < nums2.length`).

Implement the `FindSumPairs` class:
- `FindSumPairs(int[] nums1, int[] nums2)` Initializes the `FindSumPairs` object with two integer arrays `nums1` and `nums2`.
- `void add(int index, int val)` Adds `val` to `nums2[index]`.
- `int count(int tot)` Returns the number of pairs `(i, j)` such that `nums1[i] + nums2[j] == tot`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output:
[null, 8, null, 2, 1, null, null, 11]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add`: O(1)
- `count`: O(len(nums1)) because len(nums1) <= 1000 while len(nums2) <= 100000.
Space Complexity: O(len(nums2)) for frequency map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Since `len(nums1) <= 1000` is small, iterate through `nums1`:
Maintain a frequency map `counts2: Counter[int]` of `nums2`.
- `add(index, val)`: decrement count of old `nums2[index]`, add `val`, increment count of new value in `counts2`.
- `count(tot)`: sum `counts2[tot - x]` for each `x` in `nums1` in O(len(nums1)) time.
"""

import unittest
from collections import Counter


class FindSumPairs:
    """Two-array sum pair frequency counter with dynamic updates to nums2."""

    def __init__(self, nums1: list[int], nums2: list[int]) -> None:
        self.nums1: list[int] = nums1
        self.nums2: list[int] = nums2
        self.counts2: Counter[int] = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.counts2[old_val] -= 1
        new_val = old_val + val
        self.nums2[index] = new_val
        self.counts2[new_val] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for x in self.nums1:
            ans += self.counts2[tot - x]
        return ans
class TestFindSumPairs(unittest.TestCase):
    def test_example_1(self) -> None:
        fsp = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
        self.assertEqual(fsp.count(7), 8)
        fsp.add(3, 2)
        self.assertEqual(fsp.count(8), 2)
        self.assertEqual(fsp.count(4), 1)
        fsp.add(0, 1)
        fsp.add(1, 1)
        self.assertEqual(fsp.count(7), 11)


if __name__ == "__main__":
    unittest.main()
