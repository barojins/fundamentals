"""
LeetCode 1724: Checking Existence of Edge Length Limited Paths II
Difficulty: Hard
Tags: Tree, Union Find, Graph, Binary Search, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
An undirected graph of `n` nodes is defined by `edgeList`, where `edgeList[i] = [u_i, v_i, dis_i]` denotes an edge between nodes `u_i` and `v_i` with distance `dis_i`. There may be multiple edges between two nodes, and the graph may not be connected.

Implement the `DistanceLimitedPathsExist` class:
- `DistanceLimitedPathsExist(int n, int[][] edgeList)` Initializes the object with the graph.
- `boolean query(int p, int q, int limit)` Returns `true` if there is a path between `p` and `q` such that every edge on the path has a distance strictly less than `limit`, and `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["DistanceLimitedPathsExist", "query", "query", "query", "query"]
[[6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]], [2, 3, 2], [1, 3, 3], [2, 0, 3], [0, 5, 6]]
Output:
[null, true, false, true, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(E log E + N log N) Kruskal's MST + Binary Lifting with maximum edge weights on tree.
- `query`: O(log N) LCA path query.
Space Complexity: O(N log N) for binary lifting and max weight jump tables.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
1. Build Minimum Spanning Forest (MSF) using Kruskal's algorithm on edges sorted by weight.
2. In the resulting tree(s), the bottleneck edge on the path between `p` and `q` is minimized.
3. Use Binary Lifting on the MST:
   - `up[u][i]`: `2^i`-th ancestor of node `u`.
   - `max_weight[u][i]`: maximum edge weight along the jump to `up[u][i]`.
4. `query(p, q, limit)` finds LCA(p, q), computes maximum edge on tree path, and returns `max_edge < limit`.
"""

import unittest
class DSU:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False


class DistanceLimitedPathsExist:
    """MST + Binary Lifting for online distance-limited path queries."""

    def __init__(self, n: int, edgeList: list[list[int]]) -> None:
        self.n: int = n
        self.LOG: int = 18
        sorted_edges = sorted(edgeList, key=lambda e: e[2])

        # Build MST
        dsu = DSU(n)
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in sorted_edges:
            if dsu.union(u, v):
                adj[u].append((v, w))
                adj[v].append((u, w))

        self.up: list[list[int]] = [[-1] * self.LOG for _ in range(n)]
        self.max_w: list[list[int]] = [[0] * self.LOG for _ in range(n)]
        self.depth: list[int] = [0] * n
        self.comp: list[int] = [-1] * n

        # DFS for binary lifting
        comp_id = 0
        for i in range(n):
            if self.comp[i] == -1:
                stack = [(i, -1, 0, 0, comp_id)]
                while stack:
                    curr, p, w, d, c = stack.pop()
                    self.comp[curr] = c
                    self.depth[curr] = d
                    self.up[curr][0] = p
                    self.max_w[curr][0] = w
                    for nxt, weight in adj[curr]:
                        if nxt != p:
                            stack.append((nxt, curr, weight, d + 1, c))
                comp_id += 1

        for j in range(1, self.LOG):
            for i in range(n):
                anc = self.up[i][j - 1]
                if anc != -1:
                    self.up[i][j] = self.up[anc][j - 1]
                    self.max_w[i][j] = max(
                        self.max_w[i][j - 1], self.max_w[anc][j - 1]
                    )

    def query(self, p: int, q: int, limit: int) -> bool:
        if self.comp[p] != self.comp[q]:
            return False

        max_edge = 0
        if self.depth[p] < self.depth[q]:
            p, q = q, p

        # Lift p to same depth as q
        diff = self.depth[p] - self.depth[q]
        for j in range(self.LOG):
            if (diff >> j) & 1:
                max_edge = max(max_edge, self.max_w[p][j])
                p = self.up[p][j]

        if p == q:
            return max_edge < limit

        for j in range(self.LOG - 1, -1, -1):
            if self.up[p][j] != self.up[q][j]:
                max_edge = max(max_edge, self.max_w[p][j], self.max_w[q][j])
                p = self.up[p][j]
                q = self.up[q][j]

        max_edge = max(max_edge, self.max_w[p][0], self.max_w[q][0])
        return max_edge < limit

class TestDistanceLimitedPathsExist(unittest.TestCase):
    def test_example_1(self) -> None:
        dlp = DistanceLimitedPathsExist(
            6, [[0, 2, 4], [0, 3, 2], [1, 2, 3], [2, 3, 1], [4, 5, 5]]
        )
        self.assertTrue(dlp.query(2, 3, 2))
        self.assertFalse(dlp.query(1, 3, 3))
        self.assertTrue(dlp.query(2, 0, 3))
        self.assertFalse(dlp.query(0, 5, 6))


if __name__ == "__main__":
    unittest.main()
