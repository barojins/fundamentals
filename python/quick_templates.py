# pyright: basic
"""코딩 테스트에서 바로 쓰는 최소 템플릿."""

from collections import deque
from heapq import heappop, heappush, nlargest
from itertools import count


# 빈도수 — O(n)
def frequencies(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


# 투 포인터: 정렬된 배열의 두 수 합 — O(n)
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


# 고정 슬라이딩 윈도우 — O(n)
def max_window_sum(nums, k):
    window = sum(nums[:k])
    answer = window

    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        answer = max(answer, window)

    return answer


# 가변 슬라이딩 윈도우: 중복 없는 최장 부분 문자열 — O(n)
def longest_unique_substring(text):
    last = {}
    left = answer = 0

    for right, char in enumerate(text):
        left = max(left, last.get(char, -1) + 1)
        last[char] = right
        answer = max(answer, right - left + 1)

    return answer


# 누적 합 — 생성 O(n), 구간 합 O(1)
def prefix_sums(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]


# 카데인: 최대 부분 배열 합 — O(n)
def max_subarray(nums):
    current = answer = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        answer = max(answer, current)

    return answer


# 이진 탐색 — O(log n)
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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 연결 리스트 뒤집기 — O(n)
def reverse_list(head):
    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev, head = head, next_node

    return prev


# 빠른/느린 포인터: 사이클 탐지 — O(n)
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# 단조 스택: 다음으로 큰 값 — O(n)
def next_greater(nums):
    answer = [-1] * len(nums)
    stack = []

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)

    return answer


# 재귀 DFS — O(V + E)
def dfs_recursive(graph, start):
    order = []
    visited = set()

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        order.append(node)

        for next_node in graph.get(node, []):
            dfs(next_node)

    dfs(start)
    return order


# 반복 DFS — O(V + E)
def dfs_iterative(graph, start):
    order = []
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))

    return order


# BFS — O(V + E)
def bfs(graph, start):
    order = []
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)

        for next_node in graph.get(node, []):
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

    return order


# 백트래킹: 모든 부분집합 — O(n * 2^n)
def subsets(nums):
    answer = []
    path = []

    def backtrack(i):
        if i == len(nums):
            answer.append(path[:])
            return

        backtrack(i + 1)
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()

    backtrack(0)
    return answer


# 상위 K개 — O(n log k)
def top_k(nums, k):
    return nlargest(k, nums)


# 구간 병합 — O(n log n)
def merge_intervals(intervals):
    answer = []

    for start, end in sorted(intervals):
        if not answer or start > answer[-1][1]:
            answer.append([start, end])
        else:
            answer[-1][1] = max(answer[-1][1], end)

    return answer


# 다익스트라: 음수 가중치 없음 — O((V + E) log V)
def dijkstra(graph, start):
    distances = {start: 0}
    sequence = count()
    heap = [(0, next(sequence), start)]

    while heap:
        distance, _, node = heappop(heap)

        if distance != distances[node]:
            continue

        for next_node, weight in graph.get(node, []):
            new_distance = distance + weight

            if new_distance < distances.get(next_node, float("inf")):
                distances[next_node] = new_distance
                heappush(heap, (new_distance, next(sequence), next_node))

    return distances


# DP: 최소 동전 개수 — O(amount * len(coins))
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total:
                dp[total] = min(dp[total], dp[total - coin] + 1)

    return -1 if dp[amount] > amount else dp[amount]
