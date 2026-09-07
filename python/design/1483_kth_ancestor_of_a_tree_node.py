"""
LeetCode 1483: Kth Ancestor of a Tree Node
Difficulty: Hard
Tags: Tree, Binary Search, Dynamic Programming, Bit Manipulation, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of `i-th` node. The root of the tree is node `0`.

Find the `k-th` ancestor of a given node. The `k-th` ancestor of a tree node is the `k-th` node in the path that leads from that node up to the root.

Implement the `TreeAncestor` class:
- `TreeAncestor(int n, int[] parent)` Initializes the object with the number of nodes `n` and the array `parent`.
- `int getKthAncestor(int node, int k)` Returns the `k-th` ancestor of the given node. If there is no such ancestor, return `-1`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
Output:
[null,1,0,-1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N log N) binary lifting table construction.
- `getKthAncestor`: O(log k)
Space Complexity: O(N log N) for binary lifting jump table `up[node][power]`.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use Binary Lifting (jump pointers of powers of 2):
`up[node][i]` stores the `2^i`-th ancestor of `node`.
Recurrence:
`up[node][i] = up[up[node][i-1]][i-1]`
To query `k`-th ancestor:
For each bit `i` set in `k`:
jump `node = up[node][i]`. If node becomes `-1`, return `-1`.
"""

import unittest
class TreeAncestor:
    """O(log K) k-th tree ancestor query using binary lifting."""

    def __init__(self, n: int, parent: list[int]) -> None:
        self.LOG: int = 18  # 2^17 > 100,000
        self.up: list[list[int]] = [[-1] * self.LOG for _ in range(n)]

        for node in range(n):
            self.up[node][0] = parent[node]

        for j in range(1, self.LOG):
            for node in range(n):
                ancestor = self.up[node][j - 1]
                if ancestor != -1:
                    self.up[node][j] = self.up[ancestor][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        curr = node
        for j in range(self.LOG):
            if (k >> j) & 1:
                curr = self.up[curr][j]
                if curr == -1:
                    break
        return curr
class TestTreeAncestor(unittest.TestCase):
    def test_example_1(self) -> None:
        ta = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
        self.assertEqual(ta.getKthAncestor(3, 1), 1)
        self.assertEqual(ta.getKthAncestor(5, 2), 0)
        self.assertEqual(ta.getKthAncestor(6, 3), -1)


if __name__ == "__main__":
    unittest.main()
