"""
LeetCode 1993: Operations on Tree
Difficulty: Medium
Tags: Tree, Depth-First Search, Breadth-First Search, Design, Hash Table

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of the `i-th` node. The root of the tree is node `0`.

Implement the `LockingTree` class:
- `LockingTree(int[] parent)` Initializes the object with the `parent` array.
- `lock(int num, int user)`: Locks node `num` with `user`. Returns `true` if locked, `false` if already locked.
- `unlock(int num, int user)`: Unlocks node `num` if currently locked by `user`. Returns `true` if unlocked, `false` otherwise.
- `upgrade(int num, int user)`: Upgrades node `num` for `user`. Locks `num` with `user` and unlocks all its descendants if:
  1. `num` is unlocked.
  2. It has at least one locked descendant (by any user).
  3. It does not have any locked ancestors.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
Output:
[null, true, false, true, true, true, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `lock`, `unlock`: O(1)
- `upgrade`: O(N) to traverse ancestors and descendants.
Space Complexity: O(N) for tree representations.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain `locked: dict[int, int]` mapping `node -> user`.
For `upgrade(num, user)`:
1. `num not in locked`
2. Walk ancestors from `num` to root: ensure none are locked.
3. DFS descendants of `num`: check if at least one descendant is locked.
4. Unlock all descendants and set `locked[num] = user`.
"""

import unittest
from collections import defaultdict


class LockingTree:
    """Tree node locking, unlocking, and atomic subtree upgrade manager."""

    def __init__(self, parent: list[int]) -> None:
        self.parent: list[int] = parent
        self.children: dict[int, list[int]] = defaultdict(list)
        for child, p in enumerate(parent):
            if p != -1:
                self.children[p].append(child)
        self.locked: dict[int, int] = {}  # node -> user

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num) != user:
            return False
        del self.locked[num]
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # Condition 1: Node must be unlocked
        if num in self.locked:
            return False

        # Condition 3: No locked ancestors
        curr = self.parent[num]
        while curr != -1:
            if curr in self.locked:
                return False
            curr = self.parent[curr]

        # Condition 2: At least one locked descendant
        locked_descendants: list[int] = []

        def find_locked(node: int) -> None:
            for child in self.children[node]:
                if child in self.locked:
                    locked_descendants.append(child)
                find_locked(child)

        find_locked(num)
        if not locked_descendants:
            return False

        # Apply upgrade
        for d in locked_descendants:
            if d in self.locked:
                del self.locked[d]
        self.locked[num] = user
        return True
class TestLockingTree(unittest.TestCase):
    def test_example_1(self) -> None:
        tree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
        self.assertTrue(tree.lock(2, 2))
        self.assertFalse(tree.unlock(2, 3))
        self.assertTrue(tree.unlock(2, 2))
        self.assertTrue(tree.lock(4, 5))
        self.assertTrue(tree.upgrade(0, 1))
        self.assertFalse(tree.lock(0, 1))


if __name__ == "__main__":
    unittest.main()
