import unittest

from python.templates import (
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


class TemplateTests(unittest.TestCase):
    def test_array_and_string_patterns(self) -> None:
        self.assertEqual(frequencies(("a", "b", "a")), {"a": 2, "b": 1})
        self.assertEqual(two_sum_sorted((1, 2, 4, 6), 8), (1, 3))
        self.assertEqual(max_window_sum((2, 1, 5, 1, 3, 2), 3), 9)
        self.assertEqual(longest_unique_substring("😀a😀"), 2)
        prefix = prefix_sums((2, 4, 1, 3))
        self.assertEqual(range_sum(prefix, 1, 3), 8)
        self.assertEqual(max_subarray((-2, 1, -3, 4, -1, 2, 1, -5, 4)), 6)
        self.assertEqual(binary_search((1, 3, 5, 7), 5), 2)
        self.assertEqual(next_greater((2, 1, 2, 4, 3)), [4, 2, 4, -1, -1])

    def test_linked_list_patterns(self) -> None:
        head = ListNode(1, ListNode(2, ListNode(3)))
        reversed_head = reverse_list(head)
        if reversed_head is None:
            self.fail("reversing a non-empty list returned None")
        values: list[int] = []
        current = reversed_head
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [3, 2, 1])
        self.assertFalse(has_cycle(reversed_head))

        cycle = ListNode(1, ListNode(2))
        second = cycle.next
        if second is None:
            self.fail("cycle fixture is missing its second node")
        second.next = cycle
        self.assertTrue(has_cycle(cycle))

    def test_graph_patterns(self) -> None:
        graph = {"A": ("B", "C"), "B": ("D",), "C": ("D",), "D": ()}
        self.assertEqual(dfs_recursive(graph, "A"), ["A", "B", "D", "C"])
        self.assertEqual(dfs_iterative(graph, "A"), ["A", "B", "D", "C"])
        self.assertEqual(bfs(graph, "A"), ["A", "B", "C", "D"])

        weighted = {1: ((2, 4), (3, 1)), 3: ((2, 2),), 2: ()}
        self.assertEqual(dijkstra(weighted, 1), {1: 0, 3: 1, 2: 3})

    def test_combinatorial_patterns(self) -> None:
        self.assertEqual(subsets((1, 2)), [[], [2], [1], [1, 2]])
        self.assertEqual(top_k((3, 1, 5, 2, 4), 3), [5, 4, 3])
        self.assertEqual(
            merge_intervals(((1, 3), (2, 6), (8, 10))),
            [[1, 6], [8, 10]],
        )
        self.assertEqual(coin_change((1, 2, 5), 11), 3)
        self.assertEqual(coin_change((2,), 3), -1)

    def test_coin_change_rejects_invalid_inputs(self) -> None:
        for coins, amount in (((1,), -1), ((0, 1), 3), ((-1, 2), 3)):
            with self.subTest(coins=coins, amount=amount), self.assertRaises(ValueError):
                coin_change(coins, amount)


if __name__ == "__main__":
    unittest.main()
