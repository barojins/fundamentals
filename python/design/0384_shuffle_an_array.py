"""
LeetCode 384: Shuffle an Array
Difficulty: Medium
Tags: Array, Math, Design, Randomized

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given an integer array `nums`, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the `Solution` class:
- `Solution(int[] nums)` Initializes the object with the integer array `nums`.
- `int[] reset()` Resets the array to its original configuration and returns it.
- `int[] shuffle()` Returns a random shuffling of the array.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output:
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `reset()`: O(N) copy
- `shuffle()`: O(N) using Fisher-Yates shuffle algorithm
Space Complexity: O(N) to preserve original configuration.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store `self.original = list(nums)` and `self.current = list(nums)`.
- `reset()`: set `self.current = list(self.original)` and return it.
- `shuffle()`: implement Fisher-Yates: for i from n-1 down to 1, swap `current[i]` with `current[random.randint(0, i)]`.
"""

import random
import unittest


class Solution:
    """Fisher-Yates uniform array shuffling and resetting."""

    def __init__(self, nums: list[int]) -> None:
        self.original: list[int] = list(nums)
        self.current: list[int] = list(nums)

    def reset(self) -> list[int]:
        self.current = list(self.original)
        return self.current

    def shuffle(self) -> list[int]:
        n = len(self.current)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.current[i], self.current[j] = self.current[j], self.current[i]
        return self.current


class TestSolution(unittest.TestCase):
    def test_example_1(self) -> None:
        nums = [1, 2, 3]
        s = Solution(nums)
        shuffled = s.shuffle()
        self.assertEqual(sorted(shuffled), sorted(nums))
        self.assertEqual(s.reset(), [1, 2, 3])

    def test_single_element(self) -> None:
        s = Solution([42])
        self.assertEqual(s.shuffle(), [42])
        self.assertEqual(s.reset(), [42])


if __name__ == "__main__":
    unittest.main()
