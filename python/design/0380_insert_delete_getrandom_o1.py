"""
LeetCode 380: Insert Delete GetRandom O(1)
Difficulty: Medium
Tags: Array, Hash Table, Math, Design, Randomized

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Implement the `RandomizedSet` class:
- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average `O(1)` time complexity.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output:
[null, true, false, true, 2, true, false, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `insert(val)`: O(1) average
- `remove(val)`: O(1) average (swap with last element in list)
- `getRandom()`: O(1) (`random.choice`)
Space Complexity: O(N) to store N elements.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Combine a dynamic array `list` and a hash map `val_to_index: dict[int, int]`.
- On `insert(val)`: append `val` to `list`, store `val_to_index[val] = len(list) - 1`.
- On `remove(val)`: swap `val` with the last element in `list`, update index in map, then `list.pop()` and delete from map.
- On `getRandom()`: return `random.choice(self.list)`.
"""

import random
import unittest


class RandomizedSet:
    """Dynamic set supporting O(1) insert, remove, and uniform getRandom."""

    def __init__(self) -> None:
        self.nums: list[int] = []
        self.pos: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last_val = self.nums[-1]
        self.nums[idx] = last_val
        self.pos[last_val] = idx
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


class TestRandomizedSet(unittest.TestCase):
    def test_example_1(self) -> None:
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.remove(2))
        self.assertTrue(rs.insert(2))
        self.assertIn(rs.getRandom(), [1, 2])
        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.insert(2))
        self.assertEqual(rs.getRandom(), 2)

    def test_repeated_insert_remove(self) -> None:
        rs = RandomizedSet()
        self.assertTrue(rs.insert(10))
        self.assertTrue(rs.insert(20))
        self.assertTrue(rs.insert(30))
        self.assertTrue(rs.remove(20))
        self.assertFalse(rs.remove(20))
        self.assertIn(rs.getRandom(), [10, 30])


if __name__ == "__main__":
    unittest.main()
