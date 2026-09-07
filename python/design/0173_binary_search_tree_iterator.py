"""
LeetCode 173: Binary Search Tree Iterator
Difficulty: Medium
Tags: Stack, Tree, Binary Search Tree, Binary Tree, Iterator, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):

- `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class.
- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.
- `int next()` Moves the pointer to the right, then returns the number at the pointer.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output:
[null, 3, 7, true, 9, true, 15, true, 20, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next()`: O(1) amortized.
- `hasNext()`: O(1).
Space Complexity: O(h) memory on stack where h is tree height.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain a stack of nodes representing the current path in in-order traversal.
In constructor, push all leftmost ancestors of `root`.
On `next()`, pop the top node `node`. If `node.right` exists, push all leftmost ancestors of `node.right`. Return `node.val`.
"""

import unittest


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


class BSTIterator:
    """In-order BST iterator with O(h) memory and O(1) amortized next()."""

    def __init__(self, root: TreeNode | None) -> None:
        self.stack: list[TreeNode] = []
        self._push_left(root)

    def _push_left(self, node: TreeNode | None) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class TestBSTIterator(unittest.TestCase):
    def test_example_1(self) -> None:
        root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        itr = BSTIterator(root)
        self.assertEqual(itr.next(), 3)
        self.assertEqual(itr.next(), 7)
        self.assertTrue(itr.hasNext())
        self.assertEqual(itr.next(), 9)
        self.assertTrue(itr.hasNext())
        self.assertEqual(itr.next(), 15)
        self.assertTrue(itr.hasNext())
        self.assertEqual(itr.next(), 20)
        self.assertFalse(itr.hasNext())

    def test_single_node(self) -> None:
        root = TreeNode(42)
        itr = BSTIterator(root)
        self.assertTrue(itr.hasNext())
        self.assertEqual(itr.next(), 42)
        self.assertFalse(itr.hasNext())

    def test_left_skewed_tree(self) -> None:
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        itr = BSTIterator(root)
        vals = []
        while itr.hasNext():
            vals.append(itr.next())
        self.assertEqual(vals, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
