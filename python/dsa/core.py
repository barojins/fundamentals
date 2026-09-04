"""DSA foundations worth reconstructing from memory."""
# pyright: reportMissingParameterType=false, reportUnknownParameterType=false
# pyright: reportUnknownArgumentType=false, reportUnknownLambdaType=false
# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false

from collections import deque  # noqa: F401
from heapq import heappop, heappush, nlargest  # noqa: F401
from itertools import count  # noqa: F401


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


# WHEN: Find a pair in a sorted array with a target sum.
# NEED: nums is sorted in nondecreasing order.
# INVARIANT: Every discarded pair cannot reach target.
# MEMORIZE: move left up when total is small; right down when large.
# COST: O(n) time, O(1) space.
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


# WHEN: Find the largest sum among fixed-size contiguous windows.
# NEED: 1 <= k <= len(nums).
# INVARIANT: window is the sum of nums[right-k+1:right+1].
# MEMORIZE: add incoming value; subtract outgoing value.
# COST: O(n) time, O(1) space.
def max_window_sum(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("invalid window size")
    window = sum(nums[:k])
    answer = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        answer = max(answer, window)
    return answer


# WHEN: Measure the longest substring without repeated characters.
# NEED: Text is indexable and characters are hashable.
# INVARIANT: text[left:right+1] has unique characters.
# MEMORIZE: left = max(left, last.get(char, -1) + 1)
# COST: O(n) time, O(u) space.
def longest_unique_substring(text):
    last = {}
    left = answer = 0
    for right, char in enumerate(text):
        left = max(left, last.get(char, -1) + 1)
        last[char] = right
        answer = max(answer, right - left + 1)
    return answer


# WHEN: Precompute contiguous range sums for repeated queries.
# NEED: nums supports iteration and addition.
# INVARIANT: prefix[i] is the sum of nums before index i.
# MEMORIZE: prefix.append(prefix[-1] + num)
# COST: O(n) time, O(n) space.
def prefix_sums(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix


# WHEN: Answer an inclusive range-sum query from prefix sums.
# NEED: prefix was built by prefix_sums; 0 <= left <= right.
# INVARIANT: prefix[right + 1] includes exactly through right.
# MEMORIZE: sum(left..right) = prefix[right+1] - prefix[left]
# COST: O(1) time, O(1) space.
def range_sum(prefix, left, right):
    if left < 0 or right < left or right + 1 >= len(prefix):
        raise ValueError("invalid range bounds")
    return prefix[right + 1] - prefix[left]


# WHEN: Find the maximum sum of a nonempty contiguous subarray.
# NEED: nums is nonempty.
# INVARIANT: current is the best subarray sum ending at this position.
# MEMORIZE: current = max(num, current + num)
# COST: O(n) time, O(1) space.
def max_subarray(nums):
    if not nums:
        raise ValueError("nums is empty")
    current = answer = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        answer = max(answer, current)
    return answer


# WHEN: Locate a target in a sorted array.
# NEED: nums is sorted in nondecreasing order.
# INVARIANT: If target exists, it remains in [left, right].
# MEMORIZE: compare nums[mid], then halve the search interval.
# COST: O(log n) time, O(1) space.
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


# WHEN: Find the first position whose value is at least target.
# NEED: nums is sorted in nondecreasing order.
# INVARIANT: Answer remains in [left, right]; discarded values are too small.
# MEMORIZE: nums[mid] < target moves left; otherwise move right.
# COST: O(log n) time, O(1) space.
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


# WHEN: Find each element's next strictly greater value to its right.
# NEED: nums is iterable and indexable.
# INVARIANT: stack holds unresolved indices in decreasing value order.
# MEMORIZE: pop while nums[stack[-1]] < num, then push current index.
# COST: O(n) time, O(n) space.
def next_greater(nums):
    answer = [-1] * len(nums)
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)
    return answer


# WHEN: Combine overlapping or touching inclusive intervals.
# NEED: Outer/pair containers are list/tuple; endpoints are mutually orderable; start <= end.
# INVARIANT: answer is merged and sorted for all processed intervals.
# MEMORIZE: append disjoint; otherwise extend answer[-1][1].
# COST: O(n log n) time, O(n) space.
def merge_intervals(intervals):
    if not isinstance(intervals, (list, tuple)):
        raise ValueError("intervals must be a list or tuple")
    answer = []
    normalized = []
    for interval in intervals:
        if not isinstance(interval, (list, tuple)) or len(interval) != 2:
            raise ValueError("interval must contain start and end")
        start, end = interval
        normalized.append((start, end))
    for start, end in sorted(normalized):
        if start > end:
            raise ValueError("interval start exceeds end")
        if not answer or start > answer[-1][1]:
            answer.append([start, end])
        else:
            answer[-1][1] = max(answer[-1][1], end)
    return answer


# WHEN: Return the k largest values from an iterable.
# NEED: k is non-negative.
# INVARIANT: Heap-based selection retains the largest requested values.
# MEMORIZE: nlargest(k, nums) returns descending order.
# COST: O(n log k) time, O(k) space.
def top_k(nums, k):
    if k < 0:
        raise ValueError("k must be non-negative")
    return nlargest(k, nums)


# WHEN: Model or construct a singly linked list.
# NEED: next is a ListNode or None.
# INVARIANT: each node stores one value and one next-node reference.
# MEMORIZE: node.val holds data; node.next links the remaining list.
# COST: O(1) construction time and space.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# WHEN: Reverse a singly linked list in place.
# NEED: head is a ListNode or None.
# INVARIANT: prev is the reversed prefix; head is the unprocessed suffix.
# MEMORIZE: save next; point head backward; advance both pointers.
# COST: O(n) time, O(1) space.
def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev, head = head, next_node
    return prev


# WHEN: Detect whether a singly linked list contains a cycle.
# NEED: head is a ListNode or None.
# INVARIANT: slow advances one step and fast advances two steps.
# MEMORIZE: equal pointers imply the fast pointer lapped the slow pointer.
# COST: O(n) time, O(1) space.
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# WHEN: Represent a binary-tree node for traversal patterns.
# NEED: left and right are TreeNode instances or None.
# INVARIANT: each node stores its value and its two child references.
# MEMORIZE: node.left and node.right are the recursive branches.
# COST: O(1) construction time and space.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# WHEN: Visit a binary tree in root-left-right order.
# NEED: root is a TreeNode or None.
# INVARIANT: answer contains preorder values for every processed subtree.
# MEMORIZE: append node, then recurse left and right.
# COST: O(n) time, O(h) recursion space.
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


# WHEN: Visit a binary tree in left-root-right order without recursion.
# NEED: root is a TreeNode or None.
# INVARIANT: stack stores ancestors whose left subtrees are processed.
# MEMORIZE: push left spine; pop, visit, then move right.
# COST: O(n) time, O(h) space.
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


# WHEN: Visit a binary tree in left-right-root order.
# NEED: root is a TreeNode or None.
# INVARIANT: answer contains postorder values for every processed subtree.
# MEMORIZE: recurse left and right, then append node.
# COST: O(n) time, O(h) recursion space.
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


# WHEN: Visit a binary tree one depth level at a time.
# NEED: root is a TreeNode or None.
# INVARIANT: queue contains exactly the frontier for the next levels.
# MEMORIZE: process the current queue length as one level.
# COST: O(n) time, O(w) space.
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


# WHEN: Visit every vertex reachable from start in depth-first order.
# NEED: Hashable adjacency; neighbor-only keys may be absent; output is reachable only.
# INVARIANT: visited contains exactly the vertices already emitted.
# MEMORIZE: pop, skip visited, emit, then push neighbors in reverse order.
# COST: O(V + E) time, O(V + E) space.
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


# WHEN: Visit every vertex reachable from start in breadth-first order.
# NEED: Hashable adjacency; neighbor-only keys may be absent; output is reachable only.
# INVARIANT: queue holds the discovered frontier in nondecreasing distance.
# MEMORIZE: mark when enqueued; pop from the left and enqueue unseen neighbors.
# COST: O(V + E) time, O(V) space.
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


# WHEN: Find all open cells reachable from a grid start.
# NEED: 0 marks passable cells; movement is four-directional; grid is rectangular.
# INVARIANT: visited contains exactly processed reachable open cells.
# MEMORIZE: pop a cell, mark it, and push each in-bounds open neighbor.
# COST: O(rows * cols) time, O(rows * cols) space.
def grid_dfs(grid, start):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    if any(len(row) != cols for row in grid):
        raise ValueError("grid must be rectangular")
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


# WHEN: Find minimum four-directional moves between open grid cells.
# NEED: 0 marks passable cells; grid is rectangular; endpoints must be in bounds and passable.
# INVARIANT: queue processes cells by nondecreasing distance from start.
# MEMORIZE: mark on enqueue; return when goal is reached.
# COST: O(rows * cols) time, O(rows * cols) space.
def grid_bfs_distance(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    if any(len(row) != cols for row in grid):
        raise ValueError("grid must be rectangular")
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


# WHEN: Order directed vertices so every edge points forward.
# NEED: Non-negative integer node count; endpoints are in-range integer indices.
# INVARIANT: indegree counts incoming edges not yet removed.
# MEMORIZE: enqueue zero-indegree vertices; remove edges and enqueue new zeros.
# COST: O(V + E) time, O(V + E) space.
def topological_sort(num_nodes, edges):
    if num_nodes < 0:
        raise ValueError("num_nodes must be non-negative")
    edges = list(edges)
    for source, target in edges:
        if not (0 <= source < num_nodes and 0 <= target < num_nodes):
            raise ValueError("edge endpoint out of bounds")
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


# WHEN: Maintain connected components under repeated merges.
# NEED: Non-negative integer size; operation nodes are in-range integer indices.
# INVARIANT: each set has one representative root.
# MEMORIZE: compress paths in find; attach the lower-rank root.
# COST: O(alpha(n)) amortized per operation, O(n) space.
class UnionFind:
    def __init__(self, size):
        if size < 0:
            raise ValueError("size must be non-negative")
        self.parent = list(range(size))
        self.rank = [0] * size

    def _validate_node(self, node):
        if not 0 <= node < len(self.parent):
            raise ValueError("node out of bounds")

    def find(self, node):
        self._validate_node(node)
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


# WHEN: Find shortest distances from one source to every reachable vertex.
# NEED: Non-negative weights; neighbor-only keys may be absent; output is reachable only.
# INVARIANT: the smallest live heap distance is final when popped.
# MEMORIZE: relax edges; use a stale-entry check for lazy heap updates.
# COST: O((V + E) log V) time, O(V + E) space.
def dijkstra(graph, start):
    normalized_graph = {node: list(edges) for node, edges in graph.items()}
    for edges in normalized_graph.values():
        if any(weight < 0 for _, weight in edges):
            raise ValueError("Dijkstra requires non-negative weights")
    distances = {start: 0}
    sequence = count()
    heap = [(0, next(sequence), start)]
    while heap:
        distance, _, node = heappop(heap)
        if distance != distances[node]:
            continue
        for neighbor, weight in normalized_graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                heappush(heap, (candidate, next(sequence), neighbor))
    return distances


# WHEN: Include or exclude every item to generate all subsets.
# NEED: nums is an indexable sequence of values.
# INVARIANT: path stores decisions made before index; recurse twice and undo.
# MEMORIZE: branch without the item, then branch with it.
# COST: O(n * 2^n) time, O(n) space excluding output.
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


# WHEN: Generate every ordering of the input items.
# NEED: nums is an indexable sequence of values.
# INVARIANT: used[i] says whether item i is already in path.
# MEMORIZE: choose an unused item, recurse, then undo the choice.
# COST: O(n * n!) time, O(n) space excluding output.
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


# WHEN: Choose exactly size items without regard to order.
# NEED: size is non-negative; nums is an indexable sequence of values.
# INVARIANT: future choices start after the last chosen index.
# MEMORIZE: append a choice, recurse from index + 1, then pop it.
# COST: O(size * C(n, size)) time, O(size) space excluding output.
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


# WHEN: Maximize a sum using no adjacent items.
# NEED: nums is an iterable of comparable numeric values; selecting no items is allowed.
# INVARIANT: rolling states are best totals through the previous two prefixes.
# MEMORIZE: keep the old best or take this value plus the best before it.
# COST: O(n) time, O(1) space.
def max_non_adjacent_sum(nums):
    previous_two = previous_one = 0
    for num in nums:
        previous_two, previous_one = previous_one, max(previous_one, previous_two + num)
    return previous_one


# WHEN: Find the minimum right/down path sum in a grid.
# NEED: grid is a non-empty list or tuple; each row is a non-empty list or tuple of equal length.
# INVARIANT: dp[col] is the best cost to the current cell after update.
# MEMORIZE: current cost is value plus the cheaper above/left predecessor.
# COST: O(rows * cols) time, O(cols) space.
def min_grid_path_sum(grid):
    if not isinstance(grid, (list, tuple)):
        raise ValueError("grid must be a list or tuple")
    try:
        if not grid or not isinstance(grid[0], (list, tuple)) or not grid[0]:
            raise ValueError("grid must be non-empty")
        cols = len(grid[0])
    except (TypeError, IndexError):
        raise ValueError("grid must be non-empty") from None
    for row in grid:
        if not isinstance(row, (list, tuple)):
            raise ValueError("grid rows must be lists or tuples")
        row_length = len(row)
        if row_length != cols:
            raise ValueError("grid must be rectangular")
    dp = [float("inf")] * cols
    dp[0] = 0
    for row in grid:
        for col, value in enumerate(row):
            from_above = dp[col]
            from_left = dp[col - 1] if col else float("inf")
            dp[col] = value + min(from_above, from_left)
    return dp[-1]


# WHEN: Maximize value when each positive-weight item is used once.
# NEED: weights and values have equal length; capacity is non-negative.
# INVARIANT: descending capacity prevents reusing the current item.
# MEMORIZE: dp[current] keeps the best value within that capacity.
# COST: O(items * capacity) time, O(capacity) space.
def knapsack_01(weights, values, capacity):
    if len(weights) != len(values) or capacity < 0 or any(weight <= 0 for weight in weights):
        raise ValueError("invalid knapsack input")
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values, strict=True):
        for current in range(capacity, weight - 1, -1):
            dp[current] = max(dp[current], dp[current - weight] + value)
    return dp[capacity]


# WHEN: Find the fewest reusable coins for an exact amount.
# NEED: coins are positive; amount is non-negative.
# INVARIANT: dp[total] is the best exact construction of total so far.
# MEMORIZE: try each coin and extend the best solution for total - coin.
# COST: O(amount * coins) time, O(amount) space.
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


# WHEN: Select a maximum-size set of non-overlapping half-open intervals.
# NEED: Outer/pair containers are list/tuple; endpoints are mutually orderable; start <= end.
# INVARIANT: earliest finish leaves maximal room for later choices.
# MEMORIZE: sort by end and accept intervals starting at last_end or later.
# COST: O(n log n) time, O(n) space.
def interval_schedule(intervals):
    if not isinstance(intervals, (list, tuple)):
        raise ValueError("intervals must be a list or tuple")
    chosen = []
    has_last_end = False
    last_end = None
    normalized = []
    for interval in intervals:
        try:
            if not isinstance(interval, (list, tuple)) or len(interval) != 2:
                raise ValueError("interval must contain start and end")
            start, end = interval
        except (TypeError, ValueError):
            raise ValueError("interval must contain start and end") from None
        normalized.append((start, end))
    for start, end in sorted(normalized, key=lambda interval: interval[1]):
        if start > end:
            raise ValueError("interval start exceeds end")
        if not has_last_end or start >= last_end:
            chosen.append((start, end))
            has_last_end = True
            last_end = end
    return chosen
