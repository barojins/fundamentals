"""
LeetCode 398: Random Pick Index
Difficulty: Medium
Tags: Array, Hash Table, Math, Design, Reservoir Sampling, Randomized

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given an integer array `nums` with possible duplicates, randomly output the index of a given `target` number. You can assume that the given target number must exist in the array.

Implement the `Solution` class:
- `Solution(int[] nums)` Initializes the object with the array `nums`.
- `int pick(int target)` Picks a random index `i` from `nums` where `nums[i] == target`. If there are multiple valid indices, each index should have an equal probability of returning.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output:
[null, 4, 0, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `Solution(nums)`: O(N) or O(1) if streaming
- `pick(target)`: O(1) via hash map or O(N) with Reservoir Sampling
Space Complexity: O(N) for indices map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store `self.indices: dict[int, list[int]]` mapping each value to a list of its indices.
On `pick(target)`:
- Return `random.choice(self.indices[target])` in O(1) time.
"""

from collections import defaultdict
import random
import unittest


class Solution:
    """Randomly picks an index of a target number with uniform probability."""

    def __init__(self, nums: list[int]) -> None:
        self.indices: dict[int, list[int]] = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])


class TestSolution(unittest.TestCase):
    def test_example_1(self) -> None:
        nums = [1, 2, 3, 3, 3]
        s = Solution(nums)
        self.assertEqual(s.pick(1), 0)
        self.assertEqual(s.pick(2), 1)
        self.assertIn(s.pick(3), [2, 3, 4])

    def test_all_identical(self) -> None:
        nums = [5, 5, 5, 5]
        s = Solution(nums)
        for _ in range(10):
            self.assertIn(s.pick(5), [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
