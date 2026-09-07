"""
LeetCode 307: Range Sum Query - Mutable
Difficulty: Medium
Tags: Array, Design, Binary Indexed Tree, Segment Tree

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Mutable 1D range sum query.

Implement `NumArray`:
- `void update(int index, int val)`
- `int sumRange(int left, int right)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: nums = [1, 3, 5], sumRange(0, 2) -> 9, update(1, 2), sumRange(0, 2) -> 8

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `update`, `sumRange`: O(log N)
Space Complexity: O(N) Fenwick tree.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Binary Indexed Tree (Fenwick Tree).
"""

import unittest


class NumArray:
    """Mutable 1D range sum query using a Binary Indexed Tree (Fenwick Tree)."""

    def __init__(self, nums: list[int]) -> None:
        self.n: int = len(nums)
        self.nums: list[int] = list(nums)
        self.tree: list[int] = [0] * (self.n + 1)

        for i, val in enumerate(nums):
            self._add(i + 1, val)

    def _add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def _query(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)


class TestNumArrayMutable(unittest.TestCase):
    def test_example_1(self) -> None:
        na = NumArray([1, 3, 5])
        self.assertEqual(na.sumRange(0, 2), 9)
        na.update(1, 2)
        self.assertEqual(na.sumRange(0, 2), 8)


if __name__ == "__main__":
    unittest.main()
