"""
LeetCode 1600: Throne Inheritance
Difficulty: Medium
Tags: Tree, Depth-First Search, Design, Hash Table

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A kingdom consists of a king, his children, his grandchildren, and so on. Every natural person has a unique name.

Implement the `ThroneInheritance` class:
- `ThroneInheritance(string kingName)` Initializes the object of the class.
- `void birth(string parentName, string childName)` A child is born.
- `void death(string name)` The person named `name` dies.
- `string[] getInheritanceOrder()` Returns a list representing the current order of inheritance, excluding dead members.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
Output:
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `birth`, `death`: O(1)
- `getInheritanceOrder`: O(N) pre-order DFS
Space Complexity: O(N) for tree adjacency list and dead set.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Model royal family as an N-ary tree:
- `children: dict[str, list[str]]` maps parent to ordered list of children.
- `dead: set[str]` tracks deceased members.
`getInheritanceOrder()` runs standard Pre-Order DFS from `kingName`, including person in the order only if `person not in dead`.
"""

import unittest
from collections import defaultdict


class ThroneInheritance:
    """Royal family inheritance order determined by pre-order DFS traversal."""

    def __init__(self, kingName: str) -> None:
        self.king: str = kingName
        self.children: dict[str, list[str]] = defaultdict(list)
        self.dead: set[str] = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> list[str]:
        order: list[str] = []

        def dfs(person: str) -> None:
            if person not in self.dead:
                order.append(person)
            for child in self.children[person]:
                dfs(child)

        dfs(self.king)
        return order

class TestThroneInheritance(unittest.TestCase):
    def test_example_1(self) -> None:
        t = ThroneInheritance("king")
        t.birth("king", "andy")
        t.birth("king", "bob")
        t.birth("king", "catherine")
        t.birth("andy", "matthew")
        t.birth("bob", "alex")
        t.birth("bob", "asha")
        self.assertEqual(
            t.getInheritanceOrder(),
            ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"],
        )
        t.death("bob")
        self.assertEqual(
            t.getInheritanceOrder(),
            ["king", "andy", "matthew", "alex", "asha", "catherine"],
        )


if __name__ == "__main__":
    unittest.main()
