"""
LeetCode 2502: Design Memory Allocator
Difficulty: Medium
Tags: Array, Hash Table, Design, Simulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given an integer `n` representing the size of a 0-indexed memory array. All memory units are initially free.

Implement the `Allocator` class:
- `Allocator(int n)` Initializes an `Allocator` object with a memory array of size `n`.
- `int allocate(int size, int mID)` Finds the first contiguous free memory block of size `size`, marks units with `mID`, and returns the first index of the block. If no block exists, returns `-1`.
- `int freeMemory(int mID)` Frees all memory units with the given `mID` and returns the number of units freed.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
Output:
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `allocate`: O(N)
- `freeMemory`: O(N)
Space Complexity: O(N) for memory buffer.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use an array `memory = [0] * n` where `0` represents free memory.
- `allocate(size, mID)`: scan for contiguous subarray of `0`s of length `size`. Fill with `mID` and return start index.
- `freeMemory(mID)`: replace all entries matching `mID` with `0` and count occurrences.
"""

import unittest
class Allocator:
    """Contiguous block memory allocator with ID-based deallocation."""

    def __init__(self, n: int) -> None:
        self.memory: list[int] = [0] * n
        self.n: int = n

    def allocate(self, size: int, mID: int) -> int:
        free_count = 0
        start_idx = -1

        for i in range(self.n):
            if self.memory[i] == 0:
                free_count += 1
                if free_count == size:
                    start_idx = i - size + 1
                    break
            else:
                free_count = 0

        if start_idx != -1:
            for j in range(start_idx, start_idx + size):
                self.memory[j] = mID
            return start_idx

        return -1

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                self.memory[i] = 0
                count += 1
        return count
class TestAllocator(unittest.TestCase):
    def test_example_1(self) -> None:
        loc = Allocator(10)
        self.assertEqual(loc.allocate(1, 1), 0)
        self.assertEqual(loc.allocate(1, 2), 1)
        self.assertEqual(loc.allocate(1, 3), 2)
        self.assertEqual(loc.freeMemory(2), 1)
        self.assertEqual(loc.allocate(3, 4), 3)
        self.assertEqual(loc.allocate(1, 1), 1)
        self.assertEqual(loc.allocate(1, 1), 6)
        self.assertEqual(loc.freeMemory(1), 3)
        self.assertEqual(loc.allocate(10, 2), -1)
        self.assertEqual(loc.freeMemory(7), 0)


if __name__ == "__main__":
    unittest.main()
