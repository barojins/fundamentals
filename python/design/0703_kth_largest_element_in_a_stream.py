"""
LeetCode 703: Kth Largest Element in a Stream
Difficulty: Easy
Tags: Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a class to find the `kth` largest element in a stream. Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Implement the `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `kth` largest element in the stream.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
[null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N log k)
- `add`: O(log k)
Space Complexity: O(k) for the min-heap.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain a min-heap of size `k`.
The root of the min-heap `heap[0]` is always the `k`-th largest element.
When adding `val`:
- Push `val` into min-heap.
- If heap size exceeds `k`, pop the smallest element.
"""

import unittest
import heapq


class KthLargest:
    """Maintains the k-th largest element using a min-heap of size k."""

    def __init__(self, k: int, nums: list[int]) -> None:
        self.k: int = k
        self.heap: list[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
class TestKthLargest(unittest.TestCase):
    def test_example_1(self) -> None:
        kl = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kl.add(3), 4)
        self.assertEqual(kl.add(5), 5)
        self.assertEqual(kl.add(10), 5)
        self.assertEqual(kl.add(9), 8)
        self.assertEqual(kl.add(4), 8)


if __name__ == "__main__":
    unittest.main()
