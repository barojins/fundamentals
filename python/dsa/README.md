# Python DSA Templates

## Core vs. Complete
[`core.py`](core.py) is for active recall. `complete/` is the categorized reference
built in the next phases. Core is selected by transfer value, not by a target count.

## Recall Loop
1. Read the problem and name the signal.
2. State the preconditions.
3. Say the invariant without looking.
4. Write the state initialization and update.
5. Trace a three-to-five-element example.
6. State time and space complexity.
7. Change one assumption and identify the required variant.

## Learning Order
Collections -> array patterns -> binary search -> stack/queue -> linked lists ->
trees -> graph traversal -> backtracking -> dynamic programming -> weighted graphs
-> advanced structures.

## Choosing an Array Pattern
- Sorted pair or inward scan: two pointers.
- Contiguous fixed-size range: fixed window.
- Contiguous range maintained by a condition: variable window.
- Many immutable range-sum queries: prefix sum.
- Monotonic decision space: binary search.

## Choosing a Graph Algorithm
- Minimum edges in an unweighted graph: BFS.
- Edge weights only 0 or 1: 0-1 BFS (Complete).
- Non-negative edge weights: Dijkstra.
- Negative edges: Bellman-Ford (Complete).
- All-pairs shortest paths on a small dense graph: Floyd-Warshall (Complete).

## Reconstructing a Forgotten Template
Write the data structure, define what each stored value means, state the invariant,
initialize the smallest valid state, write one transition, and only then write the
return value.

## Catalog

### Arrays and searching
- [`frequencies`](core.py): count hashable values.
- [`two_sum_sorted`](core.py): find a target pair in sorted input.
- [`max_window_sum`](core.py): scan fixed-size contiguous windows.
- [`longest_unique_substring`](core.py): maintain a valid variable-size window.
- [`prefix_sums`](core.py) / [`range_sum`](core.py): preprocess inclusive range sums.
- [`max_subarray`](core.py): find the best non-empty contiguous sum.
- [`binary_search`](core.py) / [`lower_bound`](core.py): exact and boundary search.
- [`next_greater`](core.py): resolve next-greater queries with a monotonic stack.
- [`merge_intervals`](core.py): merge overlapping or touching inclusive intervals.
- [`top_k`](core.py): retain the largest k values with a heap.

### Linked structures and trees
- [`ListNode`](core.py), [`reverse_list`](core.py), [`has_cycle`](core.py): essential
  singly linked-list patterns.
- [`TreeNode`](core.py), [`preorder`](core.py), [`inorder_iterative`](core.py),
  [`postorder`](core.py), [`level_order`](core.py):
  essential binary-tree traversals.

### Graphs and grids
- [`dfs_graph`](core.py) / [`bfs_graph`](core.py): depth-first and breadth-first
  traversal.
- [`grid_dfs`](core.py) / [`grid_bfs_distance`](core.py): four-directional grid
  traversal.
- [`topological_sort`](core.py): Kahn's algorithm over integer vertex indices.
- [`UnionFind`](core.py): path-compressed connectivity over integer indices.
- [`dijkstra`](core.py): single-source shortest paths with non-negative weights.

Graph traversal and Dijkstra results contain only vertices reachable from the start.
Neighbor-only vertices do not need their own adjacency keys.

### Search generation, DP, and greedy
- [`subsets`](core.py), [`permutations`](core.py), [`combinations`](core.py): reusable
  backtracking shapes.
- [`max_non_adjacent_sum`](core.py): rolling 1D dynamic programming with an empty
  selection allowed.
- [`min_grid_path_sum`](core.py): space-optimized grid dynamic programming.
- [`knapsack_01`](core.py) / [`coin_change`](core.py): single-use and reusable-choice
  DP.
- [`interval_schedule`](core.py): earliest-finish selection for half-open `[start, end)`
  intervals; touching intervals are compatible.
