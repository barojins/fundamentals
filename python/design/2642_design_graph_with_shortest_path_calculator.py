"""
LeetCode 2642: Design Graph With Shortest Path Calculator
Difficulty: Hard
Tags: Graph, Design, Heap (Priority Queue), Shortest Path

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
There is a directed weighted graph that consists of `n` nodes labeled from `0` to `n - 1`.

Implement the `Graph` class:
- `Graph(int n, int[][] edges)` Initializes the object with `n` nodes and `edges`.
- `void addEdge(int[] edge)` Adds an edge from `edge[0]` to `edge[1]` with cost `edge[2]`.
- `int shortestPath(int node1, int node2)` Returns the minimum cost to go from `node1` to `node2`, or `-1` if no path exists.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output:
[null, 6, -1, null, 6]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addEdge`: O(1)
- `shortestPath`: O((V + E) log V) Dijkstra's algorithm.
Space Complexity: O(V + E) for adjacency list.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use Dijkstra's algorithm with a min-heap on the weighted directed adjacency list `adj: list[list[tuple[int, int]]]`.
Terminate early once `curr == node2`.
"""

import unittest
import heapq


class Graph:
    """Directed weighted graph with Dijkstra shortest path calculation."""

    def __init__(self, n: int, edges: list[list[int]]) -> None:
        self.n: int = n
        self.adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float("inf")] * self.n
        dist[node1] = 0
        heap: list[tuple[int, int]] = [(0, node1)]

        while heap:
            d, u = heapq.heappop(heap)
            if u == node2:
                return d
            if d > dist[u]:
                continue
            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (int(dist[v]), v))

        return -1

class TestGraph(unittest.TestCase):
    def test_example_1(self) -> None:
        g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
        self.assertEqual(g.shortestPath(3, 2), 6)
        self.assertEqual(g.shortestPath(0, 3), -1)
        g.addEdge([1, 3, 4])
        self.assertEqual(g.shortestPath(0, 3), 6)


if __name__ == "__main__":
    unittest.main()
