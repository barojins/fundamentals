"""
LeetCode 919: Complete Binary Tree Inserter
Difficulty: Medium
Tags: Tree, Breadth-First Search, Binary Tree, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the `CBTInserter` class:
- `CBTInserter(TreeNode root)` Initializes the data structure with the `root` of the complete binary tree.
- `int insert(int val)` Inserts a `TreeNode` into the tree with value `Node.val == val` so that the tree remains complete, and returns the value of the parent of the inserted `TreeNode`.
- `TreeNode get_root()` Returns the head node of the tree.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
Output:
[null, 1, 2, [1, 2, 3, 4]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N) using BFS to populate nodes missing a child.
- `insert(val)`: O(1)
- `get_root()`: O(1)
Space Complexity: O(N) to store active candidate parents in a queue.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a BFS `deque` of candidate parent nodes that have fewer than 2 children (i.e. `not node.left or not node.right`).
When inserting `val`:
- The parent is `queue[0]`.
- If `parent.left is None`: attach `parent.left = TreeNode(val)`.
- Else: attach `parent.right = TreeNode(val)` and `queue.popleft()`.
- Add new node to `queue`.
"""

import unittest
from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class CBTInserter:
    """O(1) inserter for complete binary tree using a candidate parent queue."""

    def __init__(self, root: TreeNode | None) -> None:
        self.root: TreeNode | None = root
        self.deque: deque[TreeNode] = deque()

        if root:
            bfs_queue = deque([root])
            while bfs_queue:
                node = bfs_queue.popleft()
                if not node.left or not node.right:
                    self.deque.append(node)
                if node.left:
                    bfs_queue.append(node.left)
                if node.right:
                    bfs_queue.append(node.right)

    def insert(self, val: int) -> int:
        parent = self.deque[0]
        new_node = TreeNode(val)
        if parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node
            self.deque.popleft()
        self.deque.append(new_node)
        return parent.val

    def get_root(self) -> TreeNode | None:
        return self.root
class TestCBTInserter(unittest.TestCase):
    def test_example_1(self) -> None:
        root = TreeNode(1, TreeNode(2))
        cbt = CBTInserter(root)
        self.assertEqual(cbt.insert(3), 1)
        self.assertEqual(cbt.insert(4), 2)
        self.assertEqual(cbt.get_root(), root)


if __name__ == "__main__":
    unittest.main()
