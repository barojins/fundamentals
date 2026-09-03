# pyright: basic

import unittest

from python.quick_templates import (
    ListNode,
    bfs,
    binary_search,
    coin_change,
    dfs_iterative,
    dfs_recursive,
    dijkstra,
    frequencies,
    has_cycle,
    longest_unique_substring,
    max_subarray,
    max_window_sum,
    merge_intervals,
    next_greater,
    prefix_sums,
    range_sum,
    reverse_list,
    subsets,
    top_k,
    two_sum_sorted,
)


class QuickTemplateTests(unittest.TestCase):
    def test_array_patterns(self):
        self.assertEqual(frequencies("abac"), {"a": 2, "b": 1, "c": 1})
        self.assertEqual(two_sum_sorted([1, 2, 4, 6], 8), (1, 3))
        self.assertEqual(max_window_sum([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(longest_unique_substring("abcabcbb"), 3)
        prefix = prefix_sums([2, 4, 1, 3])
        self.assertEqual(range_sum(prefix, 1, 3), 8)
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1]), 6)
        self.assertEqual(binary_search([1, 3, 5, 7], 5), 2)
        self.assertEqual(next_greater([2, 1, 2, 4, 3]), [4, 2, 4, -1, -1])

    def test_linked_list_patterns(self):
        head = reverse_list(ListNode(1, ListNode(2, ListNode(3))))
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        self.assertEqual(values, [3, 2, 1])
        self.assertFalse(has_cycle(head))

        cycle = ListNode(1, ListNode(2))
        second = cycle.next
        if second is None:
            self.fail("cycle fixture is missing its second node")
        second.next = cycle
        self.assertTrue(has_cycle(cycle))

    def test_graph_patterns(self):
        graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
        self.assertEqual(dfs_recursive(graph, "A"), ["A", "B", "D", "C"])
        self.assertEqual(dfs_iterative(graph, "A"), ["A", "B", "D", "C"])
        self.assertEqual(bfs(graph, "A"), ["A", "B", "C", "D"])

        weighted = {"A": [("B", 4), ("C", 1)], "C": [("B", 2)], "B": []}
        self.assertEqual(dijkstra(weighted, "A"), {"A": 0, "B": 3, "C": 1})

    def test_common_patterns(self):
        self.assertEqual(subsets([1, 2]), [[], [2], [1], [1, 2]])
        self.assertEqual(top_k([3, 1, 5, 2, 4], 3), [5, 4, 3])
        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10]]),
            [[1, 6], [8, 10]],
        )
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(coin_change([2], 3), -1)

    def test_invalid_inputs(self):
        for k in (0, 4):
            with self.subTest(k=k), self.assertRaises(ValueError):
                max_window_sum([1, 2, 3], k)

        with self.assertRaises(ValueError):
            max_subarray([])

        for coins, amount in (([1], -1), ([0, 1], 3), ([-1, 2], 3)):
            with self.subTest(coins=coins, amount=amount), self.assertRaises(ValueError):
                coin_change(coins, amount)


if __name__ == "__main__":
    unittest.main()
