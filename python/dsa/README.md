# Python DSA Templates

## Core vs. Complete
`core.py` is for active recall. `complete/` is the categorized reference built in
the next phases. Core is selected by transfer value, not by a target count.

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
- `frequencies`: count hashable values.
- `two_sum_sorted`: find a target pair in sorted input.
- `max_window_sum`: scan fixed-size contiguous windows.
- `longest_unique_substring`: maintain a valid variable-size window.
- `prefix_sums` / `range_sum`: preprocess inclusive range sums.
- `max_subarray`: find the best non-empty contiguous sum.
- `binary_search` / `lower_bound`: exact and boundary search.
- `next_greater`: resolve next-greater queries with a monotonic stack.
- `merge_intervals`: combine overlapping inclusive intervals.
- `top_k`: retain the largest k values with a heap.

### Linked structures and trees
- `ListNode`, `reverse_list`, `has_cycle`: essential singly linked-list patterns.
- `TreeNode`, `preorder`, `inorder_iterative`, `postorder`, `level_order`:
  essential binary-tree traversals.

### Graphs and grids
- `dfs_graph` / `bfs_graph`: depth-first and breadth-first traversal.
- `grid_dfs` / `grid_bfs_distance`: four-directional grid traversal.
- `topological_sort`: Kahn's algorithm for dependency order.
- `UnionFind`: path-compressed connectivity with union by rank.
- `dijkstra`: single-source shortest paths with non-negative weights.

### Search generation, DP, and greedy
- `subsets`, `permutations`, `combinations`: reusable backtracking shapes.
- `max_non_adjacent_sum`: rolling 1D dynamic programming.
- `min_grid_path_sum`: space-optimized grid dynamic programming.
- `knapsack_01` / `coin_change`: single-use and reusable-choice DP.
- `interval_schedule`: greedy selection by earliest finishing time.
