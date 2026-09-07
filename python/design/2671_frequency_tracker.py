"""
LeetCode 2671: Frequency Tracker
Difficulty: Medium
Tags: Hash Table, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that keeps track of the values of elements and allows you to query the frequency of any element.

Implement the `FrequencyTracker` class:
- `FrequencyTracker()`: Initializes the FrequencyTracker object.
- `void add(int number)`: Adds `number` to the data structure.
- `void deleteOne(int number)`: Deletes one occurrence of `number`.
- `bool hasFrequency(int frequency)`: Returns `true` if there is any number that appears `frequency` times, and `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]
Output:
[null, null, null, true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add`, `deleteOne`, `hasFrequency`: O(1) for all operations.
Space Complexity: O(N) for frequency maps.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain two frequency maps:
- `num_counts: Counter[int]` (number -> its count)
- `freq_counts: Counter[int]` (count -> how many distinct numbers have this count)
On `add`: decrement `freq_counts[old_f]`, increment `num_counts[num]`, increment `freq_counts[new_f]`.
`hasFrequency(f)` is `self.freq_counts[f] > 0` in O(1).
"""

import unittest
from collections import Counter


class FrequencyTracker:
    """O(1) value frequency tracker."""

    def __init__(self) -> None:
        self.num_counts: Counter[int] = Counter()
        self.freq_counts: Counter[int] = Counter()

    def add(self, number: int) -> None:
        old_freq = self.num_counts[number]
        if old_freq > 0:
            self.freq_counts[old_freq] -= 1
        new_freq = old_freq + 1
        self.num_counts[number] = new_freq
        self.freq_counts[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        old_freq = self.num_counts[number]
        if old_freq > 0:
            self.freq_counts[old_freq] -= 1
            new_freq = old_freq - 1
            if new_freq > 0:
                self.num_counts[number] = new_freq
                self.freq_counts[new_freq] += 1
            else:
                del self.num_counts[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_counts[frequency] > 0
class TestFrequencyTracker(unittest.TestCase):
    def test_example_1(self) -> None:
        ft = FrequencyTracker()
        ft.add(3)
        ft.add(3)
        self.assertTrue(ft.hasFrequency(2))
        ft.deleteOne(3)
        self.assertFalse(ft.hasFrequency(2))
        self.assertTrue(ft.hasFrequency(1))


if __name__ == "__main__":
    unittest.main()
