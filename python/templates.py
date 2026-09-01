"""Compact coding-interview templates."""

from collections import deque
from heapq import heappop, heappush, nlargest
from itertools import count
from typing import Deque, Dict, Hashable, Iterable, List, Optional, Set, Tuple, TypeVar

T = TypeVar("T", bound=Hashable)


# Frequency map — O(n) time, O(n) space
def frequencies(items: Iterable[T]) -> Dict[T, int]:
    counts: Dict[T, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


# Two pointers (sorted input) — O(n) time, O(1) space
def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
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


# Fixed sliding window — O(n) time, O(1) space
def max_window_sum(nums: List[int], k: int) -> int:
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    window = sum(nums[index] for index in range(k))
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best


# Variable sliding window — O(n) time, O(n) space
def longest_unique_substring(text: str) -> int:
    last_seen: Dict[str, int] = {}
    left = best = 0
    for right, char in enumerate(text):
        left = max(left, last_seen.get(char, -1) + 1)
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


# Prefix sum — build O(n), range query O(1)
def prefix_sums(nums: List[int]) -> List[int]:
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix


def range_sum(prefix: List[int], left: int, right: int) -> int:
    return prefix[right + 1] - prefix[left]


# Kadane's algorithm — O(n) time, O(1) space
def max_subarray(nums: List[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")
    current = best = nums[0]
    for index in range(1, len(nums)):
        num = nums[index]
        current = max(num, current + num)
        best = max(best, current)
    return best


# Binary search — O(log n) time, O(1) space
def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


class ListNode:
    def __init__(self, value: int, next_node: Optional["ListNode"] = None):
        self.value = value
        self.next = next_node


# Linked-list reversal — O(n) time, O(1) space
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    previous = None
    while head:
        following = head.next
        head.next = previous
        previous, head = head, following
    return previous


# Fast and slow pointers (cycle detection) — O(n) time, O(1) space
def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


# Monotonic stack (next greater value) — O(n) time, O(n) space
def next_greater(nums: List[int]) -> List[int]:
    answer = [-1] * len(nums)
    stack: List[int] = []
    for index, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(index)
    return answer


# Recursive DFS — O(V + E) time, O(V) space
def dfs_recursive(graph: Dict[T, List[T]], start: T) -> List[T]:
    order: List[T] = []
    seen: Set[T] = set()

    def visit(node: T) -> None:
        if node in seen:
            return
        seen.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return order


# Iterative DFS — O(V + E) time, O(V + E) space
def dfs_iterative(graph: Dict[T, List[T]], start: T) -> List[T]:
    order: List[T] = []
    seen: Set[T] = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order


# BFS — O(V + E) time, O(V) space
def bfs(graph: Dict[T, List[T]], start: T) -> List[T]:
    order: List[T] = []
    seen = {start}
    queue: Deque[T] = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return order


# Backtracking (all subsets) — O(n * 2^n) time, O(n) recursion space
def subsets(nums: List[int]) -> List[List[int]]:
    answer: List[List[int]] = []
    path: List[int] = []

    def backtrack(index: int) -> None:
        if index == len(nums):
            answer.append(path.copy())
            return
        backtrack(index + 1)
        path.append(nums[index])
        backtrack(index + 1)
        path.pop()

    backtrack(0)
    return answer


# Heap / top K — O(n log k) time, O(k) space
def top_k(nums: List[int], k: int) -> List[int]:
    return nlargest(k, nums)


# Merge intervals — O(n log n) time, O(n) space
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    merged: List[List[int]] = []
    for start, end in sorted(intervals):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


# Dijkstra (non-negative weights) — O((V + E) log V) time
def dijkstra(graph: Dict[T, List[Tuple[T, int]]], start: T) -> Dict[T, int]:
    distances: Dict[T, int] = {start: 0}
    sequence = count()
    heap: List[Tuple[int, int, T]] = [(0, next(sequence), start)]
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


# Dynamic programming (minimum coins) — O(amount * coins) time
def coin_change(coins: List[int], amount: int) -> int:
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("coins must be positive and amount non-negative")
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    return -1 if dp[amount] > amount else dp[amount]
