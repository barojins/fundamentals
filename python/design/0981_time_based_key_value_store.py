"""
LeetCode 981: Time Based Key-Value Store
Difficulty: Medium
Tags: Hash Table, String, Binary Search, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:
- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output:
[null, null, "bar", "bar", null, "bar2", "bar2"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `set`: O(1)
- `get`: O(log N) using binary search `bisect_right`.
Space Complexity: O(Total entries stored).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map each `key` to a list of `(timestamp, value)` tuples.
Since `set` operations arrive with strictly increasing timestamps, each list is naturally sorted by timestamp.
On `get(key, timestamp)`: binary search with `bisect_right` on timestamps to find the largest timestamp `<= timestamp`.
"""

import unittest
from collections import defaultdict
import bisect


class TimeMap:
    """Time-based key-value store using binary search on append-only histories."""

    def __init__(self) -> None:
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        history = self.store[key]
        # Search for timestamp
        idx = bisect.bisect_right(
            history, (timestamp, chr(127))
        ) - 1
        if idx < 0:
            return ""
        return history[idx][1]
class TestTimeMap(unittest.TestCase):
    def test_example_1(self) -> None:
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        self.assertEqual(tm.get("foo", 1), "bar")
        self.assertEqual(tm.get("foo", 3), "bar")
        tm.set("foo", "bar2", 4)
        self.assertEqual(tm.get("foo", 4), "bar2")
        self.assertEqual(tm.get("foo", 5), "bar2")


if __name__ == "__main__":
    unittest.main()
