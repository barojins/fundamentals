# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false

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


class FinalReviewRegressionTests(unittest.TestCase):
    def test_merge_intervals_rejects_non_sequence_outer_container(self):
        with self.assertRaises(ValueError):
            merge_intervals({(1, 2)})

    def test_merge_intervals_rejects_non_pair_sequence_members(self):
        with self.assertRaises(ValueError):
            merge_intervals(["12"])
        with self.assertRaises(ValueError):
            merge_intervals([{1, 2}])

    def test_merge_intervals_accepts_tuple_containers_and_nonnumeric_endpoints(self):
        self.assertEqual(
            merge_intervals((("a", "b"), ["b", "d"])),
            [["a", "d"]],
        )

    def test_interval_schedule_accepts_orderable_nonnumeric_endpoints(self):
        self.assertEqual(
            interval_schedule([("b", "c"), ("a", "b"), ("c", "d")]),
            [("a", "b"), ("b", "c"), ("c", "d")],
        )

    def test_dijkstra_materializes_one_shot_adjacency(self):
        graph = {
            "a": iter((("b", 2),)),
            "b": iter((("c", 3),)),
            "z": iter(()),
        }

        self.assertEqual(dijkstra(graph, "a"), {"a": 0, "b": 2, "c": 5})


class CoreDefiningEdgeCaseTests(unittest.TestCase):
    def test_frequencies_accepts_empty_input(self):
        self.assertEqual(frequencies([]), {})

    def test_two_sum_sorted_returns_none_when_no_pair_exists(self):
        self.assertIsNone(two_sum_sorted([1, 2, 3], 9))

    def test_max_window_sum_rejects_an_empty_window(self):
        with self.assertRaises(ValueError):
            max_window_sum([1, 2], 0)

    def test_longest_unique_substring_accepts_empty_text(self):
        self.assertEqual(longest_unique_substring(""), 0)

    def test_prefix_sums_accepts_empty_input(self):
        self.assertEqual(prefix_sums([]), [0])

    def test_range_sum_rejects_reversed_bounds(self):
        with self.assertRaises(ValueError):
            range_sum([0, 2, 5], 1, 0)

    def test_max_subarray_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            max_subarray([])

    def test_binary_search_accepts_empty_input(self):
        self.assertEqual(binary_search([], 4), -1)

    def test_lower_bound_accepts_empty_input(self):
        self.assertEqual(lower_bound([], 4), 0)

    def test_next_greater_accepts_empty_input(self):
        self.assertEqual(next_greater([]), [])

    def test_merge_intervals_accepts_empty_input(self):
        self.assertEqual(merge_intervals([]), [])

    def test_merge_intervals_rejects_reversed_ranges(self):
        with self.assertRaises(ValueError):
            merge_intervals([[3, 1]])

    def test_top_k_accepts_zero(self):
        self.assertEqual(top_k([3, 1, 2], 0), [])

    def test_list_node_defaults_to_an_isolated_zero_node(self):
        node = ListNode()
        self.assertEqual(node.val, 0)
        self.assertIsNone(node.next)

    def test_reverse_list_accepts_an_empty_list(self):
        self.assertIsNone(reverse_list(None))

    def test_has_cycle_rejects_a_single_acyclic_node(self):
        self.assertFalse(has_cycle(ListNode(1)))

    def test_tree_node_defaults_to_a_leaf(self):
        node = TreeNode()
        self.assertEqual(node.val, 0)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_preorder_accepts_an_empty_tree(self):
        self.assertEqual(preorder(None), [])

    def test_inorder_iterative_accepts_an_empty_tree(self):
        self.assertEqual(inorder_iterative(None), [])

    def test_postorder_accepts_an_empty_tree(self):
        self.assertEqual(postorder(None), [])

    def test_level_order_accepts_an_empty_tree(self):
        self.assertEqual(level_order(None), [])

    def test_dfs_graph_stays_reachable_with_missing_and_disconnected_keys(self):
        graph = {0: [1], 2: [3]}
        self.assertEqual(dfs_graph(graph, 0), [0, 1])

    def test_bfs_graph_stays_reachable_with_missing_and_disconnected_keys(self):
        graph = {0: [1], 2: [3]}
        self.assertEqual(bfs_graph(graph, 0), [0, 1])

    def test_grid_dfs_returns_empty_for_a_blocked_start(self):
        self.assertEqual(grid_dfs([[1]], (0, 0)), set())

    def test_grid_bfs_rejects_a_blocked_endpoint(self):
        self.assertEqual(grid_bfs_distance([[1]], (0, 0), (0, 0)), -1)

    def test_grid_bfs_reports_an_unreachable_goal(self):
        self.assertEqual(grid_bfs_distance([[0, 1], [1, 0]], (0, 0), (1, 1)), -1)

    def test_grid_bfs_returns_zero_when_start_equals_goal(self):
        self.assertEqual(grid_bfs_distance([[0]], (0, 0), (0, 0)), 0)

    def test_topological_sort_accepts_an_empty_graph(self):
        self.assertEqual(topological_sort(0, []), [])

    def test_union_find_rejects_access_into_an_empty_structure(self):
        groups = UnionFind(0)
        with self.assertRaises(ValueError):
            groups.find(0)

    def test_subsets_contains_the_empty_subset_for_empty_input(self):
        self.assertEqual(subsets([]), [[]])

    def test_permutations_contains_the_empty_ordering_for_empty_input(self):
        self.assertEqual(permutations([]), [[]])

    def test_combinations_contains_the_empty_choice_for_empty_input(self):
        self.assertEqual(combinations([], 0), [[]])

    def test_max_non_adjacent_sum_allows_an_empty_selection(self):
        self.assertEqual(max_non_adjacent_sum([-4, -2, -9]), 0)

    def test_max_non_adjacent_sum_accepts_empty_input(self):
        self.assertEqual(max_non_adjacent_sum([]), 0)

    def test_min_grid_path_sum_accepts_a_single_cell(self):
        self.assertEqual(min_grid_path_sum([[7]]), 7)

    def test_knapsack_01_accepts_zero_capacity(self):
        self.assertEqual(knapsack_01([1], [2], 0), 0)

    def test_coin_change_accepts_a_zero_amount(self):
        self.assertEqual(coin_change([2], 0), 0)

    def test_interval_schedule_accepts_empty_input(self):
        self.assertEqual(interval_schedule([]), [])

    def test_interval_schedule_rejects_reversed_ranges(self):
        with self.assertRaises(ValueError):
            interval_schedule([(3, 1)])


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
