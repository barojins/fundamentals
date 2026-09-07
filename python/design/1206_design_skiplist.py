"""
LeetCode 1206: Design Skiplist
Difficulty: Hard
Tags: Linked List, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a Skiplist without using any built-in libraries.

A skiplist is a data structure that takes `O(log(n))` time to add, erase and search. Comparing with treap and red-black tree, skiplist takes less code to implement and has higher concurrent performance.

Implement the `Skiplist` class:
- `Skiplist()` Initializes the skiplist object.
- `bool search(int target)` Returns `true` if the integer `target` exists in the Skiplist or `false` otherwise.
- `void add(int num)` Inserts the value `num` into the Skiplist.
- `bool erase(int num)` Removes the value `num` from the Skiplist and returns `true`. If `num` does not exist in the Skiplist, do nothing and return `false`. If there are multiple `num` values, removing any one of them is fine.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
Output:
[null, null, null, null, false, null, true, false, true, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `search`, `add`, `erase`: O(log N) average.
Space Complexity: O(N) average across skiplist levels.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Each `SkipNode` has `val: int` and `forward: list[SkipNode | None]` for forward pointers up to `MAX_LEVEL` (e.g. 16 or 32).
Random level generation uses coin flip (probability `p = 0.5`).
- `search`: traverse top-down, stepping forward while next node val < target, then drop down a level.
- `add`: keep `update` array of predecessor nodes at each level, generate random level, link new node into levels.
- `erase`: find node with target val, unlink from each level in `update` array.
"""

import unittest
import random


class SkipNode:
    def __init__(self, val: int = -1, level: int = 16) -> None:
        self.val: int = val
        self.forward: list[SkipNode | None] = [None] * level


class Skiplist:
    """Probabilistic Skiplist with O(log N) search, add, and erase."""

    MAX_LEVEL = 16
    P = 0.5

    def __init__(self) -> None:
        self.head: SkipNode = SkipNode(-1, self.MAX_LEVEL)
        self.level: int = 1

    def _random_level(self) -> int:
        lvl = 1
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < target:  # type: ignore
                curr = curr.forward[i]  # type: ignore
        curr = curr.forward[0]  # type: ignore
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update: list[SkipNode] = [self.head] * self.MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:  # type: ignore
                curr = curr.forward[i]  # type: ignore
            update[i] = curr

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl

        new_node = SkipNode(num, lvl)
        for i in range(lvl):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update: list[SkipNode] = [self.head] * self.MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:  # type: ignore
                curr = curr.forward[i]  # type: ignore
            update[i] = curr

        curr = curr.forward[0]  # type: ignore
        if not curr or curr.val != num:
            return False

        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            update[i].forward[i] = curr.forward[i]

        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1

        return True
class TestSkiplist(unittest.TestCase):
    def test_example_1(self) -> None:
        sl = Skiplist()
        sl.add(1)
        sl.add(2)
        sl.add(3)
        self.assertFalse(sl.search(0))
        sl.add(4)
        self.assertTrue(sl.search(1))
        self.assertFalse(sl.erase(0))
        self.assertTrue(sl.erase(1))
        self.assertFalse(sl.search(1))


if __name__ == "__main__":
    unittest.main()
