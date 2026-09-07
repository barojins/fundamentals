"""
LeetCode 379: Design Phone Directory
Difficulty: Medium
Tags: Array, Hash Table, Linked List, Design, Queue

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a phone directory that manages a pool of numbers with operations to provide an available number, check if a number is available, and release a number.

Implement the `PhoneDirectory` class:
- `PhoneDirectory(int maxNumbers)` Initializes the phone directory with the number of available slots `maxNumbers`.
- `int get()` Provides a number that is not assigned to anyone. Returns `-1` if no number is available.
- `bool check(int number)` Returns `true` if the number is available, and `false` otherwise.
- `void release(int number)` Recycles or releases a number back to the pool.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
[[3], [], [], [2], [], [2], [2], [2]]
Output:
[null, 0, 1, true, 2, false, null, true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `get()`: O(1)
- `check(number)`: O(1)
- `release(number)`: O(1)
Space Complexity: O(maxNumbers).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a `set` (or `collections.deque` + `set`) of available numbers initialized with `0, 1, ..., maxNumbers - 1`.
- `get()`: Pop an element from the available pool and return it.
- `check(number)`: Check membership in the available set.
- `release(number)`: Add number back to available set if `0 <= number < maxNumbers`.
"""

import unittest


class PhoneDirectory:
    """Manages allocation and release of phone numbers with O(1) operations."""

    def __init__(self, maxNumbers: int) -> None:
        self.max_numbers: int = maxNumbers
        self.available: set[int] = set(range(maxNumbers))

    def get(self) -> int:
        if not self.available:
            return -1
        return self.available.pop()

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        if 0 <= number < self.max_numbers:
            self.available.add(number)


class TestPhoneDirectory(unittest.TestCase):
    def test_example_1(self) -> None:
        directory = PhoneDirectory(3)
        n1 = directory.get()
        n2 = directory.get()
        self.assertTrue(0 <= n1 < 3)
        self.assertTrue(0 <= n2 < 3)
        self.assertNotEqual(n1, n2)
        self.assertEqual(len(directory.available), 1)

        remaining = list(directory.available)[0]
        self.assertTrue(directory.check(remaining))
        n3 = directory.get()
        self.assertEqual(n3, remaining)
        self.assertFalse(directory.check(remaining))

        directory.release(remaining)
        self.assertTrue(directory.check(remaining))

    def test_exhaustion(self) -> None:
        directory = PhoneDirectory(1)
        self.assertEqual(directory.get(), 0)
        self.assertEqual(directory.get(), -1)
        directory.release(0)
        self.assertEqual(directory.get(), 0)


if __name__ == "__main__":
    unittest.main()
