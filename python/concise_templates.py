"""
Senior Software Engineer - Algorithmic Master Templates
======================================================
Target: Python 3.14+ (Native generics, PEP 649 deferred annotations, union syntax)
"""

from collections import defaultdict, deque
import heapq


# =====================================================================
# 1. POINTERS & SLIDING WINDOW
# =====================================================================

def two_pointers_sorted(nums: list[int], target: int) -> list[int]:
    """Two Pointers (Opposite Ends). Time: O(N), Space: O(1)"""
    left, right = 0, len(nums) - 1
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return [left, right]
        if curr < target:
            left += 1
        else:
            right -= 1
    return []


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """Floyd's Fast & Slow Pointers. Time: O(N), Space: O(1)"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def sliding_window_fixed(nums: list[int], k: int) -> int:
    """Fixed-Size Sliding Window. Time: O(N), Space: O(1)"""
    if len(nums) < k:
        return 0
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum


def sliding_window_variable(s: str) -> int:
    """Variable-Size Sliding Window. Time: O(N), Space: O(K)"""
    counts: dict[str, int] = defaultdict(int)
    left = max_len = 0
    
    for right, char in enumerate(s):
        counts[char] += 1
        
        # Shrink window when constraint is violated (e.g., > 2 distinct chars)
        while len(counts) > 2:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
            
        max_len = max(max_len, right - left + 1)
    return max_len


# =====================================================================
# 2. LINKED LISTS & INTERVALS
# =====================================================================

def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    """In-Place Linked List Reversal. Time: O(N), Space: O(1)"""
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Interval Merging. Time: O(N log N), Space: O(N)"""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged


# =====================================================================
# 3. MONOTONIC STACK & MONOTONIC QUEUE
# =====================================================================

def next_greater_elements(nums: list[int]) -> list[int]:
    """Monotonic Decreasing Stack. Time: O(N), Space: O(N)"""
    n = len(nums)
    res = [-1] * n
    stack: list[int] = []  # Stores indices
    
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            prev_idx = stack.pop()
            res[prev_idx] = nums[i]
        stack.append(i)
    return res


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Monotonic Decreasing Deque. Time: O(N), Space: O(K)"""
    dq: deque[int] = deque()  # Stores indices
    res: list[int] = []
    
    for i, num in enumerate(nums):
        if dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


# =====================================================================
# 4. BINARY SEARCH
# =====================================================================

def binary_search_boundary(low: int, high: int) -> int:
    """Binary Search on Predicate / Leftmost True. Time: O(log N), Space: O(1)"""
    def feasible(val: int) -> bool:
        return val >= 42  # Predicate condition

    left, right = low, high
    ans = high
    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


# =====================================================================
# 5. TREES & BACKTRACKING
# =====================================================================

class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """Tree LCA (Post-Order). Time: O(N), Space: O(H)"""
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


def backtrack_subsets(nums: list[int]) -> list[list[int]]:
    """Backtracking (Subsets / Combinations). Time: O(2^N), Space: O(N)"""
    res: list[list[int]] = []
    
    def backtrack(start_idx: int, path: list[int]) -> None:
        res.append(path.copy())
        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
    backtrack(0, [])
    return res


# =====================================================================
# 6. GRAPH ALGORITHMS
# =====================================================================

def topological_sort(num_nodes: int, edges: list[list[int]]) -> list[int]:
    """Kahn's Algorithm (Topological Sort). Time: O(V + E), Space: O(V + E)"""
    adj: dict[int, list[int]] = defaultdict(list)
    indegree = [0] * num_nodes
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
        
    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    order: list[int] = []
    
    while queue:
        curr = queue.popleft()
        order.append(curr)
        for neighbor in adj[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return order if len(order) == num_nodes else []


def dijkstra(num_nodes: int, adj: dict[int, list[tuple[int, int]]], start: int) -> dict[int, float | int]:
    """Dijkstra's Shortest Path. Time: O((V + E) log V), Space: O(V + E)"""
    distances: dict[int, float | int] = {i: float("inf") for i in range(num_nodes)}
    distances[start] = 0
    pq: list[tuple[float | int, int]] = [(0, start)]  # (cost, node)
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in adj.get(curr_node, []):
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances


class UnionFind:
    """Disjoint Set Union (Path Compression & Rank). Time: O(alpha(N))"""
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [1] * size
        self.components = size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        self.components -= 1
        return True


# =====================================================================
# 7. HEAPS & TRIES
# =====================================================================

class MedianFinder:
    """Two-Heap Streaming Median. Add: O(log N), Find: O(1), Space: O(N)"""
    def __init__(self) -> None:
        self.small: list[int] = []  # Max-heap (inverted values)
        self.large: list[int] = []  # Min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    """Prefix Tree. Time: O(L), Space: O(N * L)"""
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, prefix: str) -> TrieNode | None:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# =====================================================================
# 8. DYNAMIC PROGRAMMING
# =====================================================================

def dp_1d_space_optimized(nums: list[int]) -> int:
    """1D DP (State Machine). Time: O(N), Space: O(1)"""
    if not nums:
        return 0
    dp_prev2 = 0
    dp_prev1 = nums[0]
    for i in range(1, len(nums)):
        dp_curr = max(dp_prev1, dp_prev2 + nums[i])
        dp_prev2, dp_prev1 = dp_prev1, dp_curr
    return dp_prev1


def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """0/1 Knapsack (1D Space-Optimized). Time: O(N * W), Space: O(W)"""
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[capacity]


def grid_min_path_sum(grid: list[list[int]]) -> int:
    """2D Grid DP (Space-Optimized). Time: O(M * N), Space: O(N)"""
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    dp = [float("inf")] * cols
    dp[0] = grid[0][0]
    
    for c in range(1, cols):
        dp[c] = dp[c - 1] + grid[0][c]
        
    for r in range(1, rows):
        dp[0] += grid[r][0]
        for c in range(1, cols):
            dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
            
    return int(dp[-1])