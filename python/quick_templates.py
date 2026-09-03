# pyright: basic
"""Practical coding-interview templates.

How to learn a pattern instead of memorizing random lines:
1. Recognize the question signal: sorted input, contiguous range, shortest hops, etc.
2. Check the preconditions. A correct pattern used on the wrong input is still wrong.
3. State the invariant: what remains true after every loop iteration?
4. Memorize the data structure and pointer/state updates, not the whole function.
5. Trace one tiny example by hand, then write the template again without looking.

Each memory card below answers: when to use it, what it needs, why it works,
and what to memorize. Indices returned by these templates are zero-based.
"""

from collections import deque, Counter
from heapq import heappop, heappush, nlargest
from itertools import count


# FREQUENCY MAP
# WHEN: Count occurrences, detect duplicates, or compare two collections.
# NEED: Every item must be hashable so it can be used as a dictionary key.
# WHY: After processing position i, counts stores exact frequencies through i.
# MEMORIZE: counts[x] = counts.get(x, 0) + 1. Counter(items) is the shortcut.
# COST: O(n) time, O(u) space for u unique items.
def frequencies(items):
    counts = Counter(items)
    return counts


# TWO POINTERS — PAIR SUM
# WHEN: A sorted array asks for two different elements whose sum is target.
# NEED: nums sorted ascending; otherwise pointer movement is not safe.
# WHY: A small sum eliminates left; a large sum eliminates right.
# MEMORIZE: Start at both ends and move exactly one pointer after each comparison.
# COST: O(n) time, O(1) extra space.
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


# FIXED SLIDING WINDOW
# WHEN: Find the best sum/value among every contiguous block of exactly k items.
# NEED: 1 <= k <= len(nums). "Contiguous" and fixed size are the question signals.
# WHY: The next window adds its new right item and removes its old left item.
# MEMORIZE: Build the first window once, then update with + entering - leaving.
# COST: O(n) time, O(1) extra space.
def max_window_sum(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("invalid window size")

    window = sum(nums[:k])
    answer = window

    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        answer = max(answer, window)

    return answer


# VARIABLE SLIDING WINDOW
# WHEN: Find a longest/shortest contiguous region satisfying a condition.
# EXAMPLE: "Longest substring without repeating characters."
# WHY: left is always beyond the previous occurrence, so the window stays unique.
# MEMORIZE: Expand right, repair the window by moving left, then update the answer.
# COST: O(n) time, O(u) space for u distinct characters.
def longest_unique_substring(text):
    last = {}
    left = answer = 0

    for right, char in enumerate(text):
        left = max(left, last.get(char, -1) + 1)
        last[char] = right
        answer = max(answer, right - left + 1)

    return answer


# PREFIX SUM
# WHEN: The same array has many inclusive range-sum queries [left, right].
# IDEA: prefix[i] means the sum before index i; prefix therefore starts with 0.
# WHY: Subtracting two prefixes cancels everything outside the requested range.
# MEMORIZE: range_sum = prefix[right + 1] - prefix[left].
# COST: O(n) setup, O(1) per query, O(n) space.
def prefix_sums(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]


# KADANE'S ALGORITHM
# WHEN: Find the maximum sum of a non-empty contiguous subarray.
# NEED: nums must be non-empty; negative values are allowed.
# WHY: current is the best sum ending here: start fresh or extend the previous range.
# MEMORIZE: current = max(num, current + num); answer = max(answer, current).
# COST: O(n) time, O(1) extra space.
def max_subarray(nums):
    if not nums:
        raise ValueError("nums is empty")

    current = answer = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)
        answer = max(answer, current)

    return answer


# BINARY SEARCH
# WHEN: Find a target in sorted data, or search a monotonic true/false condition.
# NEED: This exact version expects nums sorted ascending.
# WHY: Comparing the middle safely discards half of the remaining search interval.
# MEMORIZE: Inclusive bounds; while left <= right; discard mid with +/- 1.
# COST: O(log n) time, O(1) extra space.
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


# REVERSE A LINKED LIST
# WHEN: Reverse the direction of every next pointer in a singly linked list.
# WHY: prev is the already-reversed prefix; head is the next node to process.
# MEMORIZE: Save next_node before overwriting head.next, then advance both pointers.
# EDGE: An empty list returns None; one node returns itself.
# COST: O(n) time, O(1) extra space.
def reverse_list(head):
    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev, head = head, next_node

    return prev


# FAST AND SLOW POINTERS — CYCLE DETECTION
# WHEN: Determine whether repeatedly following next eventually revisits a node.
# WHY: In a cycle, the faster pointer eventually laps and meets the slower pointer.
# MEMORIZE: slow moves 1, fast moves 2; compare node identity with "is".
# EDGE: Stop when fast or fast.next is None, which proves the list ends.
# COST: O(n) time, O(1) extra space.
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# MONOTONIC STACK — NEXT GREATER VALUE
# WHEN: For every item, find the first larger value to its right.
# WHY: stack holds unresolved indices whose values are decreasing.
# MEMORIZE: While current is larger, pop and resolve; then push current index.
# EDGE: Indices left in the stack have no greater value and remain -1.
# COST: O(n) time and O(n) space; every index is pushed and popped at most once.
def next_greater(nums):
    answer = [-1] * len(nums)
    stack = []

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)

    return answer


# RECURSIVE DFS
# WHEN: Explore an entire branch before trying the next branch.
# USES: Components, reachability, trees, grids, paths, and backtracking foundations.
# WHY: visited ensures each reachable node is processed at most once, even in cycles.
# MEMORIZE: Check visited -> mark -> process -> recurse over neighbors.
# COST: O(V + E) time, O(V) space including the call stack.
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


# ITERATIVE DFS
# WHEN: Use DFS without recursion-depth risk or when explicit stack control helps.
# WHY: The stack stores discovered work; visited prevents repeated processing.
# MEMORIZE: Pop, skip if visited, mark/process, then push neighbors.
# NOTE: reversed keeps this example's visit order consistent with recursive DFS.
# COST: O(V + E) time, O(V) space.
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


# BFS
# WHEN: Explore level by level; find minimum edges in an unweighted graph.
# NEED: Use Dijkstra instead when edges have different non-negative costs.
# WHY: FIFO order visits every node at the earliest possible edge distance.
# MEMORIZE: Mark visited when enqueueing, not when dequeueing, to avoid duplicates.
# COST: O(V + E) time, O(V) space.
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


# BACKTRACKING — ALL SUBSETS
# WHEN: Generate every choice combination where each item is excluded or included.
# WHY: At index i, the two recursive branches cover both possible decisions.
# MEMORIZE: Choose -> recurse -> undo. Here, the no-choice branch comes first.
# STATE: path is the current choice; path[:] saves a snapshot, not a shared reference.
# COST: O(n * 2^n) time including copies, O(n) recursion space excluding output.
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


# TOP K WITH A HEAP
# WHEN: Return only the k largest items without sorting the entire input yourself.
# WHY: A size-k min-heap keeps only the strongest k candidates seen so far.
# MEMORIZE: In Python, nlargest(k, nums) expresses the complete pattern.
# COST: O(n log k) time and O(k) extra space for typical small k.
def top_k(nums, k):
    return nlargest(k, nums)


# MERGE INTERVALS
# WHEN: Combine overlapping ranges such as meetings, reservations, or coverage.
# NEED: Sort by start first; each interval is [start, end] with start <= end.
# WHY: After sorting, a new interval can overlap only the last merged interval.
# MEMORIZE: New gap -> append; overlap -> extend the last end with max.
# COST: O(n log n) time for sorting, O(n) output space.
def merge_intervals(intervals):
    answer = []

    for start, end in sorted(intervals):
        if not answer or start > answer[-1][1]:
            answer.append([start, end])
        else:
            answer[-1][1] = max(answer[-1][1], end)

    return answer


# DIJKSTRA'S SHORTEST PATH
# WHEN: Find minimum total cost from one start node in a weighted graph.
# NEED: Every edge weight must be non-negative. Use Bellman-Ford for negatives.
# GRAPH: graph[node] contains (neighbor, weight); unreachable nodes are absent.
# WHY: The smallest live heap distance is final; stale larger entries are skipped.
# MEMORIZE: Pop cheapest -> relax each edge -> push every improved distance.
# COST: O((V + E) log V) time, O(V + E) space with adjacency lists.
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


# DYNAMIC PROGRAMMING — MINIMUM COINS
# WHEN: Make an amount with the fewest coins; every coin may be reused.
# NEED: amount >= 0 and all coin values > 0.
# STATE: dp[total] is the minimum coins needed to make exactly total.
# WHY: The last coin is coin, so the candidate is dp[total - coin] + 1.
# MEMORIZE: Define state -> base dp[0] = 0 -> transition -> impossible check.
# COST: O(amount * len(coins)) time, O(amount) space.
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
