"""
LeetCode 1146: Snapshot Array
Difficulty: Medium
Tags: Array, Hash Table, Binary Search, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Implement a `SnapshotArray` that supports pre-set length, setting elements, taking snapshots, and getting values from historical snapshots.

Implement the `SnapshotArray` class:
- `SnapshotArray(int length)` initializes an array-like data structure with the given length. Initially, each element equals 0.
- `void set(index, val)` sets the element at the given `index` to be equal to `val`.
- `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus 1.
- `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["SnapshotArray", "set", "snap", "set", "get"]
[[3], [0, 5], [], [0, 6], [0, 0]]
Output:
[null, null, 0, null, 5]

Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0, 5);  // Set array[0] = 5
snapshotArr.snap();     // Take a snapshot, return snap_id = 0
snapshotArr.set(0, 6);
snapshotArr.get(0, 0);  // Get the value of array[0] with snap_id = 0, return 5

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `set`: O(1)
- `snap`: O(1)
- `get`: O(log S) where S is number of historical updates to index.
Space Complexity: O(Total number of set operations).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
For each index in the array, maintain an append-only history of `[(snap_id, val)]`.
Initially `history[i] = [(0, 0)]`.
- `set(index, val)`: if latest record for `index` already has current `snap_id`, overwrite it; else append `(snap_id, val)`.
- `snap()`: increment and return `snap_id`.
- `get(index, snap_id)`: binary search with `bisect_right` on `snap_id` in `history[index]`.
"""

import unittest
import bisect


class SnapshotArray:
    """Snapshot Array tracking historical mutations per index with binary search retrieval."""

    def __init__(self, length: int) -> None:
        self.snap_id: int = 0
        # For each index: list of (snap_id, val)
        self.history: list[list[tuple[int, int]]] = [
            [(0, 0)] for _ in range(length)
        ]

    def set(self, index: int, val: int) -> None:
        records = self.history[index]
        if records[-1][0] == self.snap_id:
            records[-1] = (self.snap_id, val)
        else:
            records.append((self.snap_id, val))

    def snap(self) -> int:
        curr_snap = self.snap_id
        self.snap_id += 1
        return curr_snap

    def get(self, index: int, snap_id: int) -> int:
        records = self.history[index]
        idx = bisect.bisect_right(records, (snap_id, float("inf"))) - 1
        return records[idx][1]
class TestSnapshotArray(unittest.TestCase):
    def test_example_1(self) -> None:
        sa = SnapshotArray(3)
        sa.set(0, 5)
        self.assertEqual(sa.snap(), 0)
        sa.set(0, 6)
        self.assertEqual(sa.get(0, 0), 5)
        self.assertEqual(sa.get(0, 1), 6)


if __name__ == "__main__":
    unittest.main()
