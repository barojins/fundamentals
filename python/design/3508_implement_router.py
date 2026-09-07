"""
LeetCode 3508: Implement Router
Difficulty: Medium
Tags: Trie, Hash Table, String, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Implement a network packet router with exact and wildcard route matching.

Implement the `Router` class:
- `Router(List<List<String>> routes)` Initializes with `[destination_prefix, next_hop]`.
- `void addRoute(List<String> route)` Adds a route rule.
- `void removeRoute(String destination)` Removes route.
- `String route(List<String> packet)` Matches longest prefix match for packet destination.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Router", "route", "addRoute", "route"]
[[[["192.168", "hopA"], ["192", "hopB"]]], [["192.168.1.1"]], [["192.168.1", "hopC"]], [["192.168.1.1"]]]
Output:
[null, "hopA", null, "hopC"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addRoute`, `removeRoute`: O(L)
- `route`: O(L) longest prefix match.
Space Complexity: O(Routes total length).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Trie for Longest Prefix Match (LPM) on IP/destination tokens.
"""

import unittest
class RouterNode:
    def __init__(self) -> None:
        self.children: dict[str, RouterNode] = {}
        self.next_hop: str | None = None


class Router:
    """Longest Prefix Match (LPM) Network Packet Router."""

    def __init__(self, routes: list[list[str]]) -> None:
        self.root = RouterNode()
        for r in routes:
            self.addRoute(r)

    def addRoute(self, route: list[str]) -> None:
        dest, hop = route[0], route[1]
        curr = self.root
        tokens = dest.split(".")
        for token in tokens:
            if token not in curr.children:
                curr.children[token] = RouterNode()
            curr = curr.children[token]
        curr.next_hop = hop

    def removeRoute(self, destination: str) -> None:
        curr = self.root
        tokens = destination.split(".")
        for token in tokens:
            if token not in curr.children:
                return
            curr = curr.children[token]
        curr.next_hop = None

    def route(self, packet: list[str]) -> str:
        dest = packet[0]
        tokens = dest.split(".")
        curr = self.root
        best_hop = "DEFAULT"

        for token in tokens:
            if token not in curr.children:
                break
            curr = curr.children[token]
            if curr.next_hop is not None:
                best_hop = curr.next_hop

        return best_hop
class TestRouter(unittest.TestCase):
    def test_example_1(self) -> None:
        r = Router([["192.168", "hopA"], ["192", "hopB"]])
        self.assertEqual(r.route(["192.168.1.1"]), "hopA")
        r.addRoute(["192.168.1", "hopC"])
        self.assertEqual(r.route(["192.168.1.1"]), "hopC")


if __name__ == "__main__":
    unittest.main()
