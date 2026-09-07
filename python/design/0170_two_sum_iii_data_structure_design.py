"""
LeetCode 170: Two Sum III - Data structure design
Difficulty: Easy
Tags: Array, Hash Table, Two Pointers, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that accepts a stream of integers and checks if it contains a pair of integers that sum up to a target value.

Implement the `TwoSum` class:
- `TwoSum()` Initializes the `TwoSum` object, with an initially empty list.
- `void add(int number)` Adds `number` to the data structure.
- `boolean find(int value)` Returns `true` if there exists any pair of numbers whose sum is equal to `value`, otherwise, it returns `false`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output:
[null, null, null, null, true, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add`: O(1)
- `find`: O(N) where N is the number of unique elements added.
Space Complexity: O(N) for storing counts in a hash map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a frequency map (`collections.Counter` / `dict`). For `find(value)`, iterate over all unique keys `num`. The complement is `complement = value - num`.
If `complement != num`, check if `complement in counts`.
If `complement == num`, check if `counts[num] >= 2`.
"""

import unittest
from collections import Counter


class TwoSum:
    """Data structure that accepts a stream of numbers and checks for 2-sum pairs."""

    def __init__(self) -> None:
        self.counts: Counter[int] = Counter()

    def add(self, number: int) -> None:
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        for num, count in self.counts.items():
            complement = value - num
            if complement == num:
                if count >= 2:
                    return True
            elif complement in self.counts:
                return True
        return False


class TestTwoSum(unittest.TestCase):
    def test_example_1(self) -> None:
        two_sum = TwoSum()
        two_sum.add(1)
        two_sum.add(3)
        two_sum.add(5)
        self.assertTrue(two_sum.find(4))
        self.assertFalse(two_sum.find(7))

    def test_duplicate_elements_same_number(self) -> None:
        two_sum = TwoSum()
        two_sum.add(3)
        self.assertFalse(two_sum.find(6))
        two_sum.add(3)
        self.assertTrue(two_sum.find(6))

    def test_negative_and_zero(self) -> None:
        two_sum = TwoSum()
        two_sum.add(0)
        two_sum.add(-5)
        two_sum.add(5)
        self.assertTrue(two_sum.find(0))
        self.assertTrue(two_sum.find(-5))
        self.assertFalse(two_sum.find(10))


if __name__ == "__main__":
    unittest.main()
