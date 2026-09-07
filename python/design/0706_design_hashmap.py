"""
LeetCode 706: Design HashMap
Difficulty: Easy
Tags: Array, Hash Table, Linked List, Design, Hash Function

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:
- `MyHashMap()` initializes the object with an empty map.
- `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
- `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
- `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output:
[null, null, null, 1, -1, null, 1, null, -1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `put`, `get`, `remove`: O(1) average.
Space Complexity: O(B + N) where B is bucket count.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use separate chaining where each bucket is a list of `(key, value)` pairs.
Hash function: `key % num_buckets`.
When updating, overwrite existing key's value in bucket.
"""

import unittest
class MyHashMap:
    """HashMap with separate chaining collision resolution."""

    def __init__(self) -> None:
        self.num_buckets: int = 769
        self.buckets: list[list[list[int]]] = [
            [] for _ in range(self.num_buckets)
        ]

    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for item in bucket:
            if item[0] == key:
                item[1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        for item in bucket:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        for i, item in enumerate(bucket):
            if item[0] == key:
                del bucket[i]
                return
class TestMyHashMap(unittest.TestCase):
    def test_example_1(self) -> None:
        hm = MyHashMap()
        hm.put(1, 1)
        hm.put(2, 2)
        self.assertEqual(hm.get(1), 1)
        self.assertEqual(hm.get(3), -1)
        hm.put(2, 1)
        self.assertEqual(hm.get(2), 1)
        hm.remove(2)
        self.assertEqual(hm.get(2), -1)


if __name__ == "__main__":
    unittest.main()
