"""
LeetCode 460: LFU Cache
Difficulty: Hard
Tags: Hash Table, Linked List, Doubly-Linked List, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the `LFUCache` class:
- `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
- `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
- `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

The functions `get` and `put` must each run in `O(1)` average time complexity.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `get(key)`: O(1)
- `put(key, value)`: O(1)
Space Complexity: O(capacity) to store elements across frequency buckets.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `vals: dict[int, int]`: key -> value
- `freqs: dict[int, int]`: key -> frequency
- `freq_to_keys: dict[int, OrderedDict[int, None]]`: frequency -> OrderedDict of keys (where first key is LRU for that freq)
- `min_freq: int`: tracks the lowest frequency currently present in cache.
When a key is accessed (`get` or `put` existing), increment frequency and move it from `freq_to_keys[f]` to `freq_to_keys[f + 1]`.
"""

from collections import OrderedDict, defaultdict
import unittest


class LFUCache:
    """O(1) Least Frequently Used (LFU) cache with LRU tie-breaking."""

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.vals: dict[int, int] = {}
        self.freqs: dict[int, int] = {}
        self.freq_to_keys: dict[int, OrderedDict[int, None]] = defaultdict(OrderedDict)
        self.min_freq: int = 0

    def _update_freq(self, key: int) -> None:
        f = self.freqs[key]
        self.freqs[key] = f + 1
        del self.freq_to_keys[f][key]

        if not self.freq_to_keys[f] and self.min_freq == f:
            self.min_freq += 1

        self.freq_to_keys[f + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        self._update_freq(key)
        return self.vals[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.vals:
            self.vals[key] = value
            self._update_freq(key)
            return

        if len(self.vals) >= self.capacity:
            # Evict LRU key from min_freq bucket
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.vals[evict_key]
            del self.freqs[evict_key]

        self.vals[key] = value
        self.freqs[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


class TestLFUCache(unittest.TestCase):
    def test_example_1(self) -> None:
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)  # evicts 2 (freq 1 vs freq 2)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)
        cache.put(4, 4)  # evicts 1 (tie on freq 2, 1 was LRU)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_zero_capacity(self) -> None:
        cache = LFUCache(0)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), -1)

    def test_update_frequency_on_put(self) -> None:
        cache = LFUCache(2)
        cache.put(1, 10)
        cache.put(1, 20)
        cache.put(2, 30)
        cache.put(3, 40)  # should evict key 2 because key 1 has freq 2
        self.assertEqual(cache.get(1), 20)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 40)


if __name__ == "__main__":
    unittest.main()
