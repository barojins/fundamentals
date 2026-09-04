# pyright: basic
import unittest

from python.dsa.core import (
    binary_search,
    frequencies,
    longest_unique_substring,
    lower_bound,
    max_subarray,
    max_window_sum,
    merge_intervals,
    next_greater,
    prefix_sums,
    range_sum,
    top_k,
    two_sum_sorted,
)


class LinearCoreTests(unittest.TestCase):
    def test_hash_map_and_array_patterns(self):
        self.assertEqual(frequencies("banana"), {"b": 1, "a": 3, "n": 2})
        self.assertEqual(two_sum_sorted([1, 4, 7, 9], 13), (1, 3))
        self.assertIsNone(two_sum_sorted([1, 2, 3], 9))
        self.assertEqual(max_window_sum([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(longest_unique_substring("abcabcbb"), 3)
        prefix = prefix_sums([2, -1, 4, 3])
        self.assertEqual(prefix, [0, 2, 1, 5, 8])
        self.assertEqual(range_sum(prefix, 1, 3), 6)
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5]), 6)

    def test_search_stack_interval_and_heap_patterns(self):
        nums = [1, 2, 2, 2, 5]
        self.assertIn(binary_search(nums, 2), {1, 2, 3})
        self.assertEqual(binary_search(nums, 4), -1)
        self.assertEqual(lower_bound(nums, 2), 1)
        self.assertEqual(lower_bound(nums, 4), 4)
        self.assertEqual(next_greater([2, 1, 2, 4, 3]), [4, 2, 4, -1, -1])
        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [10, 12]]),
            [[1, 6], [8, 12]],
        )
        self.assertEqual(top_k([3, 1, 5, 2, 4], 3), [5, 4, 3])

    def test_linear_preconditions(self):
        with self.assertRaises(ValueError):
            max_window_sum([1, 2], 0)
        with self.assertRaises(ValueError):
            max_subarray([])
        with self.assertRaises(ValueError):
            top_k([1, 2], -1)
        with self.assertRaises(ValueError):
            range_sum([0, 2, 1, 5, 8], -1, 2)
        with self.assertRaises(ValueError):
            range_sum([0, 2, 1, 5, 8], 1, 4)
        with self.assertRaises(ValueError):
            merge_intervals([[1, 3], []])
        with self.assertRaises(ValueError):
            merge_intervals([[1]])


if __name__ == "__main__":
    unittest.main()
