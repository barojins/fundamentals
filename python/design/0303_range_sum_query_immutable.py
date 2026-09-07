"""
LeetCode 303: Range Sum Query - Immutable
Difficulty: Easy
Tags: Array, Design, Prefix Sum

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Immutable 1D range sum query.

Implement `NumArray`:
- `NumArray(int[] nums)`
- `int sumRange(int left, int right)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
[null, 1, -1, -3]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N)
- `sumRange`: O(1)
Space Complexity: O(N)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Prefix sum array `prefix[i] = prefix[i-1] + nums[i-1]`.
"""

import unittest


class NumArray:
    """1D immutable range sum queries using prefix sums."""

    def __init__(self, nums: list[int]) -> None:
        self.prefix: list[int] = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


class TestNumArray(unittest.TestCase):
    def test_example_1(self) -> None:
        na = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(na.sumRange(0, 2), 1)
        self.assertEqual(na.sumRange(2, 5), -1)
        self.assertEqual(na.sumRange(0, 5), -3)


if __name__ == "__main__":
    unittest.main()
