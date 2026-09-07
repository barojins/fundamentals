"""
LeetCode 705: Design HashSet
Difficulty: Easy
Tags: Array, Hash Table, Linked List, Design, Hash Function

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a HashSet without using any built-in hash table libraries.

Implement the `MyHashSet` class:
- `void add(key)` Inserts the value `key` into the HashSet.
- `bool contains(key)` Returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output:
[null, null, null, true, false, null, true, null, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add`, `remove`, `contains`: O(1) average.
Space Complexity: O(B + N) where B is number of buckets and N is number of elements.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use separate chaining with a fixed prime number of buckets (e.g., 769 or 1009).
Hash function: `key % num_buckets`.
Each bucket is a list (or linked list). Search linearly within the small bucket list.
"""

import unittest
class MyHashSet:
    """HashSet with separate chaining hash collision resolution."""

    def __init__(self) -> None:
        self.num_buckets: int = 769
        self.buckets: list[list[int]] = [[] for _ in range(self.num_buckets)]

    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]
        return key in bucket
class TestMyHashSet(unittest.TestCase):
    def test_example_1(self) -> None:
        hs = MyHashSet()
        hs.add(1)
        hs.add(2)
        self.assertTrue(hs.contains(1))
        self.assertFalse(hs.contains(3))
        hs.add(2)
        self.assertTrue(hs.contains(2))
        hs.remove(2)
        self.assertFalse(hs.contains(2))


if __name__ == "__main__":
    unittest.main()
