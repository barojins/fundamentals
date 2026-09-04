"""DSA foundations worth reconstructing from memory."""
# pyright: basic

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


# WHEN: Combine overlapping or touching intervals.
# NEED: Each interval is [start, end] with start <= end.
# INVARIANT: answer is merged and sorted for all processed intervals.
# MEMORIZE: append disjoint; otherwise extend answer[-1][1].
# COST: O(n log n) time, O(n) space.
def merge_intervals(intervals):
    answer = []
    normalized = []
    for interval in intervals:
        try:
            if len(interval) != 2:
                raise ValueError("interval must contain start and end")
            start, end = interval
        except (TypeError, ValueError):
            raise ValueError("interval must contain start and end") from None
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
