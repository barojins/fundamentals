"""
LeetCode 381: Insert Delete GetRandom O(1) - Duplicates allowed
Difficulty: Hard
Tags: Array, Hash Table, Math, Design, Randomized

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
`RandomizedCollection` is a data structure that contains a collection of numbers, possibly with duplicates (i.e., a multiset).

Implement the `RandomizedCollection` class:
- `RandomizedCollection()` Initializes the `RandomizedCollection` object.
- `bool insert(int val)` Inserts an item `val` into the multiset. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the multiset if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current multiset. The probability of each element being returned is linearly proportional to the count of that element in the multiset.

You must implement the functions of the class such that each function works in average `O(1)` time complexity.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
Output:
[null, true, false, true, 2, true, 1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `insert`: O(1) average
- `remove`: O(1) average
- `getRandom`: O(1)
Space Complexity: O(N) to store multiset elements and sets of indices.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain `self.nums: list[int]` and `self.indices: dict[int, set[int]]`.
- On `insert(val)`: append `val` to `nums`, add index `len(nums) - 1` to `indices[val]`.
- On `remove(val)`:
  1. Pop an index `remove_idx` from `indices[val]`.
  2. Let `last_val = nums[-1]`, `last_idx = len(nums) - 1`.
  3. Overwrite `nums[remove_idx] = last_val`.
  4. Update `indices[last_val]`: remove `last_idx`, add `remove_idx`.
  5. Pop from `nums`.
- On `getRandom()`: `random.choice(self.nums)`.
"""

from collections import defaultdict
import random
import unittest


class RandomizedCollection:
    """Multiset supporting O(1) insert, remove, and weighted getRandom."""

    def __init__(self) -> None:
        self.nums: list[int] = []
        self.indices: dict[int, set[int]] = defaultdict(set)

    def insert(self, val: int) -> bool:
        is_new = len(self.indices[val]) == 0
        self.indices[val].add(len(self.nums))
        self.nums.append(val)
        return is_new

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False

        remove_idx = self.indices[val].pop()
        last_idx = len(self.nums) - 1
        last_val = self.nums[-1]

        if remove_idx != last_idx:
            self.nums[remove_idx] = last_val
            self.indices[last_val].remove(last_idx)
            self.indices[last_val].add(remove_idx)

        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


class TestRandomizedCollection(unittest.TestCase):
    def test_example_1(self) -> None:
        rc = RandomizedCollection()
        self.assertTrue(rc.insert(1))
        self.assertFalse(rc.insert(1))
        self.assertTrue(rc.insert(2))
        self.assertIn(rc.getRandom(), [1, 2])
        self.assertTrue(rc.remove(1))
        self.assertIn(rc.getRandom(), [1, 2])

    def test_duplicates_removal(self) -> None:
        rc = RandomizedCollection()
        self.assertTrue(rc.insert(10))
        self.assertFalse(rc.insert(10))
        self.assertTrue(rc.remove(10))
        self.assertEqual(rc.getRandom(), 10)
        self.assertTrue(rc.remove(10))
        self.assertFalse(rc.remove(10))


if __name__ == "__main__":
    unittest.main()
