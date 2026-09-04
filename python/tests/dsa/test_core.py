# pyright: basic
import unittest

from python.dsa.core import (
    ListNode,
    TreeNode,
    UnionFind,
    bfs_graph,
    binary_search,
    coin_change,
    combinations,
    dfs_graph,
    dijkstra,
    frequencies,
    grid_bfs_distance,
    grid_dfs,
    has_cycle,
    inorder_iterative,
    interval_schedule,
    knapsack_01,
    level_order,
    longest_unique_substring,
    lower_bound,
    max_non_adjacent_sum,
    max_subarray,
    max_window_sum,
    merge_intervals,
    min_grid_path_sum,
    next_greater,
    permutations,
    postorder,
    prefix_sums,
    preorder,
    range_sum,
    reverse_list,
    subsets,
    top_k,
    topological_sort,
    two_sum_sorted,
)


class CoreCatalogTests(unittest.TestCase):
    def test_every_required_core_symbol_is_public(self):
        import python.dsa.core as core

        required = {
            "frequencies",
            "two_sum_sorted",
            "max_window_sum",
            "longest_unique_substring",
            "prefix_sums",
            "range_sum",
            "max_subarray",
            "binary_search",
            "lower_bound",
            "next_greater",
            "merge_intervals",
            "top_k",
            "ListNode",
            "reverse_list",
            "has_cycle",
            "TreeNode",
            "preorder",
            "inorder_iterative",
            "postorder",
            "level_order",
            "dfs_graph",
            "bfs_graph",
            "grid_dfs",
            "grid_bfs_distance",
            "topological_sort",
            "UnionFind",
            "dijkstra",
            "subsets",
            "permutations",
            "combinations",
            "max_non_adjacent_sum",
            "min_grid_path_sum",
            "knapsack_01",
            "coin_change",
            "interval_schedule",
        }
        self.assertTrue(required <= set(vars(core)))


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


class LinkedTreeCoreTests(unittest.TestCase):
    def test_reverse_list_and_cycle(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        reversed_head = reverse_list(head)
        values = []
        while reversed_head is not None:
            values.append(reversed_head.val)
            reversed_head = reversed_head.next
        self.assertEqual(values, [3, 2, 1])

        cycle = ListNode(1, ListNode(2))
        cycle.next.next = cycle  # pyright: ignore[reportOptionalMemberAccess]
        self.assertTrue(has_cycle(cycle))
        self.assertFalse(has_cycle(ListNode(1)))

    def test_tree_traversals(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(preorder(root), [1, 2, 4, 5, 3])
        self.assertEqual(inorder_iterative(root), [4, 2, 5, 1, 3])
        self.assertEqual(postorder(root), [4, 5, 2, 3, 1])
        self.assertEqual(level_order(root), [[1], [2, 3], [4, 5]])
        self.assertEqual(level_order(None), [])


class GraphCoreTests(unittest.TestCase):
    def test_graph_and_grid_traversal(self):
        graph = {0: [1, 2], 1: [2], 2: [3], 3: []}
        self.assertEqual(dfs_graph(graph, 0), [0, 1, 2, 3])
        self.assertEqual(bfs_graph(graph, 0), [0, 1, 2, 3])
        grid = [[0, 0, 1], [1, 0, 0], [1, 1, 0]]
        self.assertEqual(grid_dfs(grid, (0, 0)), {(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)})
        self.assertEqual(grid_bfs_distance(grid, (0, 0), (2, 2)), 4)

    def test_topology_union_find_and_dijkstra(self):
        self.assertEqual(topological_sort(4, [(0, 1), (0, 2), (1, 3), (2, 3)]), [0, 1, 2, 3])
        self.assertEqual(topological_sort(2, [(0, 1), (1, 0)]), [])
        groups = UnionFind(4)
        self.assertTrue(groups.union(0, 1))
        self.assertFalse(groups.union(0, 1))
        self.assertFalse(groups.connected(0, 2))
        groups.union(1, 2)
        self.assertTrue(groups.connected(0, 2))
        graph = {"a": [("b", 4), ("c", 1)], "c": [("b", 2)], "b": []}
        self.assertEqual(dijkstra(graph, "a"), {"a": 0, "c": 1, "b": 3})

    def test_graph_preconditions(self):
        with self.assertRaises(ValueError):
            dijkstra({0: [(1, -1)]}, 0)
        with self.assertRaises(ValueError):
            UnionFind(-1)
        with self.assertRaises(ValueError):
            topological_sort(-1, [])
        with self.assertRaises(ValueError):
            topological_sort(2, [(-1, 1)])
        with self.assertRaises(ValueError):
            topological_sort(2, [(0, 2)])

        groups = UnionFind(2)
        with self.assertRaises(ValueError):
            groups.find(-1)
        with self.assertRaises(ValueError):
            groups.union(0, 2)
        with self.assertRaises(ValueError):
            groups.connected(2, 0)

        ragged_grid = [[0, 0], [0]]
        with self.assertRaises(ValueError):
            grid_dfs(ragged_grid, (0, 0))
        with self.assertRaises(ValueError):
            grid_bfs_distance(ragged_grid, (0, 0), (1, 0))


class CombinatorialCoreTests(unittest.TestCase):
    def test_backtracking(self):
        self.assertEqual(subsets([1, 2]), [[], [2], [1], [1, 2]])
        self.assertEqual(permutations([1, 2]), [[1, 2], [2, 1]])
        self.assertEqual(combinations([1, 2, 3], 2), [[1, 2], [1, 3], [2, 3]])

    def test_dynamic_programming(self):
        self.assertEqual(max_non_adjacent_sum([2, 7, 9, 3, 1]), 12)
        self.assertEqual(min_grid_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
        self.assertEqual(knapsack_01([2, 3, 4], [4, 5, 7], 5), 9)
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
        self.assertEqual(coin_change([2], 3), -1)

    def test_greedy_interval_selection(self):
        self.assertEqual(
            interval_schedule([(1, 3), (2, 4), (3, 5), (5, 7)]),
            [(1, 3), (3, 5), (5, 7)],
        )

    def test_combinatorial_preconditions(self):
        with self.assertRaises(ValueError):
            combinations([1, 2], -1)
        with self.assertRaises(ValueError):
            min_grid_path_sum([])
        with self.assertRaises(ValueError):
            knapsack_01([1], [2, 3], 4)
        with self.assertRaises(ValueError):
            coin_change([0, 1], 3)
        with self.assertRaises(ValueError):
            interval_schedule([(1,)])
        with self.assertRaises(ValueError):
            interval_schedule([1, 2])
        with self.assertRaises(ValueError):
            interval_schedule([{"start": 1, "end": 2}])
        with self.assertRaises(ValueError):
            interval_schedule(["12"])
        with self.assertRaises(ValueError):
            interval_schedule({(1, 2)})
        with self.assertRaises(ValueError):
            interval_schedule({(1, 2): "interval"})
        with self.assertRaises(ValueError):
            min_grid_path_sum([[1], 2])
        with self.assertRaises(ValueError):
            min_grid_path_sum([[1], {2}])
        with self.assertRaises(ValueError):
            min_grid_path_sum([[1], {"value": 2}])
        with self.assertRaises(ValueError):
            min_grid_path_sum({"row": [1]})
        with self.assertRaises(ValueError):
            min_grid_path_sum({(1,)})


if __name__ == "__main__":
    unittest.main()
