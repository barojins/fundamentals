"""
LeetCode 146: LRU Cache
Difficulty: Medium
Tags: Hash Table, Linked List, Doubly-Linked List, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:
- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `get(key)`: O(1)
- `put(key, value)`: O(1)
Space Complexity: O(capacity) to store at most `capacity` nodes.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Hash Map (`dict`) combined with a Doubly Linked List (with dummy `head` and `tail` sentinels).
- Map key -> Doubly Linked List Node (`key`, `val`, `prev`, `next`).
- When accessed (`get` or `put` existing), move the node to the head (most recently used).
- When capacity is exceeded on `put`, remove node from the tail (least recently used) and delete from map.
"""

import unittest


class DNode:
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key: int = key
        self.val: int = val
        self.prev: DNode | None = None
        self.next: DNode | None = None


class LRUCache:
    """Least Recently Used (LRU) Cache implementation using a Doubly Linked List + Hash Map."""

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.cache: dict[int, DNode] = {}
        self.head: DNode = DNode()  # Dummy head (MRU side)
        self.tail: DNode = DNode()  # Dummy tail (LRU side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DNode) -> None:
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    def _add_to_head(self, node: DNode) -> None:
        node.next = self.head.next
        node.prev = self.head
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                if lru_node and lru_node != self.head:
                    self._remove(lru_node)
                    del self.cache[lru_node.key]
            new_node = DNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


class TestLRUCache(unittest.TestCase):
    def test_example_1(self) -> None:
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)  # evicts key 2
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)  # evicts key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_capacity_one(self) -> None:
        cache = LRUCache(1)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        cache.put(2, 20)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 20)

    def test_update_existing_key(self) -> None:
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 10)  # update 1, 1 becomes MRU
        cache.put(3, 3)   # evicts 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 3)

    def test_get_refreshes_recency(self) -> None:
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)  # 1 is now MRU, 2 is LRU
        cache.put(3, 3)  # evicts 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)


if __name__ == "__main__":
    unittest.main()
