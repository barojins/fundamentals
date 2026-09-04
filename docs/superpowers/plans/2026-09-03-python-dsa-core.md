# Python DSA Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone, tested Python DSA core file containing the transferable patterns a coding-interview learner should be able to reconstruct from memory.

**Architecture:** `python/dsa/core.py` is deliberately standalone and grouped by concept so it can be rewritten without navigating imports. `python/dsa/README.md` explains the recall workflow and distinguishes Core from the later categorized Complete reference. Tests use the repository's existing `unittest`, Ruff, and Pyright setup.

**Tech Stack:** Python 3.12+, standard library only, `unittest`, Ruff, Pyright, uv

**Spec:** `docs/superpowers/specs/2026-09-03-python-dsa-template-set-design.md`

## Global Constraints

- Core code avoids advanced type syntax so the algorithm remains visually dominant.
- Each pattern includes `WHEN`, `NEED`, `INVARIANT`, `MEMORIZE`, and `COST` comments.
- Implementations are deterministic and do not print.
- Functions do not mutate caller input unless explicitly documented as in-place.
- Invalid structural preconditions raise `ValueError`.
- Indices are zero-based; interval endpoint semantics are explicit.
- Existing `python/quick_templates.py`, `python/templates.py`, and `python/concise_templates.py` remain unchanged.
- This plan delivers Core only. Complete reference modules follow as separate independently testable plans: linear patterns, trees/graphs, combinatorial algorithms, and advanced structures/integration.

## Memory Card Matrix

Use these exact ideas in the five comment fields. Wording may be shortened only when
the meaning and stated precondition remain unchanged.

| Symbol | WHEN / NEED | INVARIANT / MEMORIZE | COST |
|---|---|---|---|
| `frequencies` | Count or compare hashable items. | Counts are exact for the processed prefix; use `get(x, 0) + 1`. | O(n) / O(u) |
| `two_sum_sorted` | Find a pair in ascending input. | A small sum disproves `left`; a large sum disproves `right`. | O(n) / O(1) |
| `max_window_sum` | Optimize a contiguous block of exactly `k`; require `1 <= k <= n`. | Add the entering value and remove the leaving value. | O(n) / O(1) |
| `longest_unique_substring` | Longest contiguous region with no duplicate. | `left` stays beyond every repeated character in the window. | O(n) / O(u) |
| `prefix_sums`, `range_sum` | Many immutable inclusive range sums. | `prefix[i]` is the sum before `i`; subtract `prefix[right + 1] - prefix[left]`. | O(n) build, O(1) query / O(n) |
| `max_subarray` | Best non-empty contiguous sum. | `current` is the best sum ending at the current position. | O(n) / O(1) |
| `binary_search` | Exact lookup in ascending input. | The target, if present, remains in inclusive `[left, right]`. | O(log n) / O(1) |
| `lower_bound` | First index whose value is at least target. | The answer remains in half-open `[left, right]`. | O(log n) / O(1) |
| `next_greater` | First greater value to each item's right. | The stack contains unresolved indices in decreasing-value order. | O(n) / O(n) |
| `merge_intervals` | Combine valid inclusive ranges. | Sorted output is disjoint; only the last interval can overlap next. | O(n log n) / O(n) |
| `top_k` | Keep only the largest `k`; require `k >= 0`. | A size-k heap retains the strongest candidates. | O(n log k) / O(k) |
| `reverse_list` | Reverse singly linked pointers. | `prev` is the reversed prefix; save `next` before rewiring. | O(n) / O(1) |
| `has_cycle` | Detect repeated linked-list nodes. | Slow moves one and fast two; a cycle forces a meeting. | O(n) / O(1) |
| `preorder` | Process tree root before children. | Each call completely traverses its subtree in root-left-right order. | O(n) / O(h) |
| `inorder_iterative` | Traverse left-root-right without recursion. | The stack stores ancestors awaiting processing. | O(n) / O(h) |
| `postorder` | Process tree children before root. | Each call completes left and right before appending root. | O(n) / O(h) |
| `level_order` | Group tree nodes by depth. | The queue contains exactly the next frontier in FIFO order. | O(n) / O(w) |
| `dfs_graph` | Explore one graph branch fully. | The stack stores pending work; visited nodes are processed once. | O(V + E) / O(V) |
| `bfs_graph` | Explore unweighted graph levels. | Mark on enqueue so each node enters the queue once. | O(V + E) / O(V) |
| `grid_dfs` | Reachability through open four-directional cells. | Visited contains exactly the processed reachable cells. | O(rows * cols) / O(rows * cols) |
| `grid_bfs_distance` | Minimum moves through open four-directional cells. | FIFO order processes cells by nondecreasing distance. | O(rows * cols) / O(rows * cols) |
| `topological_sort` | Order directed dependencies. | Indegree counts only remaining incoming edges; zero is ready. | O(V + E) / O(V + E) |
| `UnionFind` | Repeated connectivity and merging. | Each set has one representative; compress paths and merge ranks. | O(alpha(n)) amortized / O(n) |
| `dijkstra` | Shortest paths with non-negative weights only. | The smallest live heap distance is final; relax improved edges. | O((V + E) log V) / O(V + E) |
| `subsets` | Include/exclude every item. | `path` stores decisions before index; recurse twice and undo. | O(n * 2^n) / O(n) excluding output |
| `permutations` | Generate every ordering. | `used[i]` says whether item `i` is already in `path`. | O(n * n!) / O(n) excluding output |
| `combinations` | Choose exactly `k` items without order. | Future choices start after the last chosen index. | O(k * C(n,k)) / O(k) excluding output |
| `max_non_adjacent_sum` | Optimize choices that cannot be adjacent. | Rolling states are best totals through the previous two prefixes. | O(n) / O(1) |
| `min_grid_path_sum` | Minimum right/down path in a non-empty rectangular grid. | `dp[col]` is the best cost to the current cell after update. | O(rows * cols) / O(cols) |
| `knapsack_01` | Maximize value when each positive-weight item is used once. | Descending capacity prevents reusing the current item. | O(items * capacity) / O(capacity) |
| `coin_change` | Fewest reusable positive coins for a non-negative amount. | `dp[total]` is the best exact construction of `total`. | O(amount * coins) / O(amount) |
| `interval_schedule` | Select the most non-overlapping valid intervals. | Earliest finish leaves maximal room for all later choices. | O(n log n) / O(n) |

---

### Task 1: Package and Linear Core Patterns

**Files:**
- Create: `python/dsa/__init__.py`
- Create: `python/dsa/core.py`
- Create: `python/tests/__init__.py`
- Create: `python/tests/dsa/__init__.py`
- Create: `python/tests/dsa/test_core.py`

**Interfaces:**
- Consumes: Python standard-library `collections`, `heapq`, and `itertools` modules.
- Produces: `frequencies`, `two_sum_sorted`, `max_window_sum`, `longest_unique_substring`, `prefix_sums`, `range_sum`, `max_subarray`, `binary_search`, `lower_bound`, `next_greater`, `merge_intervals`, and `top_k`.

- [ ] **Step 1: Write failing linear-pattern tests**

Create package marker files containing only a short module docstring. Create `test_core.py` with:

```python
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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and verify RED**

Run: `uv run python -m unittest python/tests/dsa/test_core.py`

Expected: FAIL because `python.dsa.core` does not exist.

- [ ] **Step 3: Implement the linear patterns with memory cards**

Create `core.py` with the imports below and implement the tested interfaces using these exact state transitions:

```python
"""DSA foundations worth reconstructing from memory."""

from collections import deque
from heapq import heappop, heappush, nlargest
from itertools import count


# WHEN: Count occurrences, detect duplicates, or compare collections.
# NEED: Items are hashable.
# INVARIANT: counts contains exact frequencies for the processed prefix.
# MEMORIZE: counts[x] = counts.get(x, 0) + 1
# COST: O(n) time, O(u) space.
def frequencies(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1
    return None


def max_window_sum(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("invalid window size")
    window = sum(nums[:k])
    answer = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        answer = max(answer, window)
    return answer


def longest_unique_substring(text):
    last = {}
    left = answer = 0
    for right, char in enumerate(text):
        left = max(left, last.get(char, -1) + 1)
        last[char] = right
        answer = max(answer, right - left + 1)
    return answer


def prefix_sums(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]


def max_subarray(nums):
    if not nums:
        raise ValueError("nums is empty")
    current = answer = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        answer = max(answer, current)
    return answer


def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def next_greater(nums):
    answer = [-1] * len(nums)
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)
    return answer


def merge_intervals(intervals):
    answer = []
    for start, end in sorted(intervals):
        if start > end:
            raise ValueError("interval start exceeds end")
        if not answer or start > answer[-1][1]:
            answer.append([start, end])
        else:
            answer[-1][1] = max(answer[-1][1], end)
    return answer


def top_k(nums, k):
    if k < 0:
        raise ValueError("k must be non-negative")
    return nlargest(k, nums)
```

Add a five-line memory card before every function using the exact ideas in the Memory Card Matrix.

- [ ] **Step 4: Run the focused tests and quality checks**

Run:

```bash
uv run python -m unittest python/tests/dsa/test_core.py
uv run ruff check python/dsa/core.py python/tests/dsa/test_core.py
uv run ruff format --check python/dsa/core.py python/tests/dsa/test_core.py
uv run pyright python/dsa/core.py python/tests/dsa/test_core.py
```

Expected: all commands exit 0; 3 tests pass.

- [ ] **Step 5: Commit the linear core**

```bash
git add python/dsa python/tests
git commit -m "feat: add linear DSA core templates"
```

---

### Task 2: Linked-List and Tree Core Patterns

**Files:**
- Modify: `python/dsa/core.py`
- Modify: `python/tests/dsa/test_core.py`

**Interfaces:**
- Consumes: the Task 1 package and test file.
- Produces: `ListNode`, `reverse_list`, `has_cycle`, `TreeNode`, `preorder`, `inorder_iterative`, `postorder`, and `level_order`.

- [ ] **Step 1: Add failing linked-list and tree tests**

Add the new imports and this test class:

```python
class LinkedTreeCoreTests(unittest.TestCase):
    def test_reverse_list_and_cycle(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        reversed_head = reverse_list(head)
        values = []
        while reversed_head:
            values.append(reversed_head.val)
            reversed_head = reversed_head.next
        self.assertEqual(values, [3, 2, 1])

        cycle = ListNode(1, ListNode(2))
        cycle.next.next = cycle
        self.assertTrue(has_cycle(cycle))
        self.assertFalse(has_cycle(ListNode(1)))

    def test_tree_traversals(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(preorder(root), [1, 2, 4, 5, 3])
        self.assertEqual(inorder_iterative(root), [4, 2, 5, 1, 3])
        self.assertEqual(postorder(root), [4, 5, 2, 3, 1])
        self.assertEqual(level_order(root), [[1], [2, 3], [4, 5]])
        self.assertEqual(level_order(None), [])
```

- [ ] **Step 2: Run the test and verify RED**

Run: `uv run python -m unittest python/tests/dsa/test_core.py`

Expected: FAIL with missing linked-list/tree imports.

- [ ] **Step 3: Implement linked-list and tree templates**

Append memory cards and these implementations to `core.py`:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev, head = head, next_node
    return prev


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    answer = []

    def dfs(node):
        if not node:
            return
        answer.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return answer


def inorder_iterative(root):
    answer, stack = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        answer.append(root.val)
        root = root.right
    return answer


def postorder(root):
    answer = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        answer.append(node.val)

    dfs(root)
    return answer


def level_order(root):
    if not root:
        return []
    answer = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        answer.append(level)
    return answer
```

- [ ] **Step 4: Run the focused tests and quality checks**

Run the four commands from Task 1 Step 4.

Expected: all commands exit 0; 5 tests pass.

- [ ] **Step 5: Commit the linked-list and tree core**

```bash
git add python/dsa/core.py python/tests/dsa/test_core.py
git commit -m "feat: add linked-list and tree core templates"
```

---

### Task 3: Graph, Grid, and Connectivity Core Patterns

**Files:**
- Modify: `python/dsa/core.py`
- Modify: `python/tests/dsa/test_core.py`

**Interfaces:**
- Consumes: `deque`, `heappop`, `heappush`, and `count` imported in Task 1.
- Produces: `dfs_graph`, `bfs_graph`, `grid_dfs`, `grid_bfs_distance`, `topological_sort`, `UnionFind`, and `dijkstra`.

- [ ] **Step 1: Add failing graph tests**

Add imports and:

```python
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
```

- [ ] **Step 2: Run the test and verify RED**

Run: `uv run python -m unittest python/tests/dsa/test_core.py`

Expected: FAIL with missing graph imports.

- [ ] **Step 3: Implement graph, grid, and connectivity templates**

Append memory cards and implement:

```python
def dfs_graph(graph, start):
    order, visited, stack = [], set(), [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order


def bfs_graph(graph, start):
    order, visited, queue = [], {start}, deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def grid_dfs(grid, start):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    row, col = start
    if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] != 0:
        return set()
    visited, stack = set(), [start]
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                stack.append((nr, nc))
    return visited


def grid_bfs_distance(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    start_row, start_col = start
    goal_row, goal_col = goal
    valid_start = 0 <= start_row < rows and 0 <= start_col < cols
    valid_goal = 0 <= goal_row < rows and 0 <= goal_col < cols
    if not valid_start or not valid_goal:
        return -1
    if grid[start_row][start_col] != 0 or grid[goal_row][goal_col] != 0:
        return -1
    if start == goal:
        return 0
    queue, visited = deque([(start_row, start_col, 0)]), {start}
    while queue:
        row, col, distance = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] != 0 or (nr, nc) in visited:
                continue
            if (nr, nc) == goal:
                return distance + 1
            visited.add((nr, nc))
            queue.append((nr, nc, distance + 1))
    return -1


def topological_sort(num_nodes, edges):
    graph = [[] for _ in range(num_nodes)]
    indegree = [0] * num_nodes
    for source, target in edges:
        graph[source].append(target)
        indegree[target] += 1
    queue = deque(node for node, degree in enumerate(indegree) if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_nodes else []


class UnionFind:
    def __init__(self, size):
        if size < 0:
            raise ValueError("size must be non-negative")
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left, right):
        root_left, root_right = self.find(left), self.find(right)
        if root_left == root_right:
            return False
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1
        return True

    def connected(self, left, right):
        return self.find(left) == self.find(right)


def dijkstra(graph, start):
    for edges in graph.values():
        if any(weight < 0 for _, weight in edges):
            raise ValueError("Dijkstra requires non-negative weights")
    distances = {start: 0}
    sequence = count()
    heap = [(0, next(sequence), start)]
    while heap:
        distance, _, node = heappop(heap)
        if distance != distances[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                heappush(heap, (candidate, next(sequence), neighbor))
    return distances
```

- [ ] **Step 4: Run the focused tests and quality checks**

Run the four commands from Task 1 Step 4.

Expected: all commands exit 0; 8 tests pass.

- [ ] **Step 5: Commit the graph core**

```bash
git add python/dsa/core.py python/tests/dsa/test_core.py
git commit -m "feat: add graph and connectivity core templates"
```

---

### Task 4: Backtracking, Dynamic Programming, and Greedy Core

**Files:**
- Modify: `python/dsa/core.py`
- Modify: `python/tests/dsa/test_core.py`

**Interfaces:**
- Consumes: no interfaces beyond Python built-ins.
- Produces: `subsets`, `permutations`, `combinations`, `max_non_adjacent_sum`, `min_grid_path_sum`, `knapsack_01`, `coin_change`, and `interval_schedule`.

- [ ] **Step 1: Add failing combinatorial tests**

Add imports and:

```python
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
```

- [ ] **Step 2: Run the test and verify RED**

Run: `uv run python -m unittest python/tests/dsa/test_core.py`

Expected: FAIL with missing combinatorial imports.

- [ ] **Step 3: Implement backtracking, DP, and greedy templates**

Append memory cards and:

```python
def subsets(nums):
    answer, path = [], []

    def backtrack(index):
        if index == len(nums):
            answer.append(path[:])
            return
        backtrack(index + 1)
        path.append(nums[index])
        backtrack(index + 1)
        path.pop()

    backtrack(0)
    return answer


def permutations(nums):
    answer, path, used = [], [], [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            answer.append(path[:])
            return
        for index, value in enumerate(nums):
            if used[index]:
                continue
            used[index] = True
            path.append(value)
            backtrack()
            path.pop()
            used[index] = False

    backtrack()
    return answer


def combinations(nums, size):
    if size < 0:
        raise ValueError("size must be non-negative")
    answer, path = [], []

    def backtrack(start):
        if len(path) == size:
            answer.append(path[:])
            return
        needed = size - len(path)
        for index in range(start, len(nums) - needed + 1):
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return answer


def max_non_adjacent_sum(nums):
    previous_two = previous_one = 0
    for num in nums:
        previous_two, previous_one = previous_one, max(previous_one, previous_two + num)
    return previous_one


def min_grid_path_sum(grid):
    if not grid or not grid[0]:
        raise ValueError("grid must be non-empty")
    cols = len(grid[0])
    if any(len(row) != cols for row in grid):
        raise ValueError("grid must be rectangular")
    dp = [float("inf")] * cols
    dp[0] = 0
    for row in grid:
        for col, value in enumerate(row):
            from_above = dp[col]
            from_left = dp[col - 1] if col else float("inf")
            dp[col] = value + min(from_above, from_left)
    return dp[-1]


def knapsack_01(weights, values, capacity):
    if len(weights) != len(values) or capacity < 0 or any(weight <= 0 for weight in weights):
        raise ValueError("invalid knapsack input")
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values, strict=True):
        for current in range(capacity, weight - 1, -1):
            dp[current] = max(dp[current], dp[current - weight] + value)
    return dp[capacity]


def coin_change(coins, amount):
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("invalid coins or amount")
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    return -1 if dp[amount] > amount else dp[amount]


def interval_schedule(intervals):
    chosen = []
    last_end = float("-inf")
    for start, end in sorted(intervals, key=lambda interval: interval[1]):
        if start > end:
            raise ValueError("interval start exceeds end")
        if start >= last_end:
            chosen.append((start, end))
            last_end = end
    return chosen
```

- [ ] **Step 4: Run the focused tests and quality checks**

Run the four commands from Task 1 Step 4.

Expected: all commands exit 0; 12 tests pass.

- [ ] **Step 5: Commit the combinatorial core**

```bash
git add python/dsa/core.py python/tests/dsa/test_core.py
git commit -m "feat: add backtracking DP and greedy core templates"
```

---

### Task 5: Core Learning Guide and Integration Verification

**Files:**
- Create: `python/dsa/README.md`
- Modify: `python/dsa/core.py`
- Modify: `python/tests/dsa/test_core.py`

**Interfaces:**
- Consumes: every public Core interface from Tasks 1-4.
- Produces: a category index, learning progression, recall loop, decision guides, and a verified standalone Core set.

- [ ] **Step 1: Add the Core completeness test**

Add:

```python
class CoreCatalogTests(unittest.TestCase):
    def test_every_required_core_symbol_is_public(self):
        import python.dsa.core as core

        required = {
            "frequencies", "two_sum_sorted", "max_window_sum",
            "longest_unique_substring", "prefix_sums", "range_sum",
            "max_subarray", "binary_search", "lower_bound", "next_greater",
            "merge_intervals", "top_k", "ListNode", "reverse_list", "has_cycle",
            "TreeNode", "preorder", "inorder_iterative", "postorder", "level_order",
            "dfs_graph", "bfs_graph", "grid_dfs", "grid_bfs_distance",
            "topological_sort", "UnionFind", "dijkstra", "subsets",
            "permutations", "combinations", "max_non_adjacent_sum",
            "min_grid_path_sum", "knapsack_01", "coin_change", "interval_schedule",
        }
        self.assertTrue(required <= set(vars(core)))
```

- [ ] **Step 2: Run the catalog test and verify GREEN**

Run: `uv run python -m unittest python/tests/dsa/test_core.py`

Expected: PASS with 13 tests. This is a completeness guard over already-developed behavior, so it is expected to pass immediately.

- [ ] **Step 3: Write the Core learning guide**

Create `README.md` with these concrete sections:

```markdown
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
```

- [ ] **Step 4: Run full scoped and repository verification**

Run:

```bash
uv run python -m unittest discover
uv run ruff check python/dsa python/tests/dsa
uv run ruff format --check python/dsa python/tests/dsa
uv run pyright python/dsa python/tests/dsa
npm --prefix typescript ci
npm --prefix typescript run check
git diff --check
```

Expected: all new DSA checks, Python tests, TypeScript checks, and whitespace checks exit 0. If the pre-existing `python/concise_templates.py` still prevents the repository-wide `check.py` command from completing, report that separately and do not modify or exclude it as part of this plan.

- [ ] **Step 5: Verify requirements against the design**

Confirm from the diff that:

- every Core symbol is covered by a test;
- every function has the five memory-card fields;
- existing template files have no diff;
- `core.py` is standalone and does not import existing templates;
- the README names Complete as a later reference phase rather than claiming it exists.

- [ ] **Step 6: Commit the learning guide**

```bash
git add python/dsa/README.md python/dsa/core.py python/tests/dsa/test_core.py
git commit -m "docs: add Python DSA core learning guide"
```

- [ ] **Step 7: Review before Complete plans**

Use `superpowers:requesting-code-review` to review Core against this plan and the design spec. Address verified findings through `superpowers:receiving-code-review`, rerun Step 4, then write the next implementation plan for `complete/arrays_strings.py`, `complete/searching_sorting.py`, `complete/linked_lists.py`, and `complete/stacks_queues.py`.
