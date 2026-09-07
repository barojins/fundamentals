"""
LeetCode 1586: Binary Search Tree Iterator II
Difficulty: Medium
Tags: Stack, Tree, Binary Search Tree, Binary Tree, Design, Iterator

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST) with bidirectional traversal capability:

- `BSTIterator(TreeNode root)` Initializes the object of the `BSTIterator` class.
- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer.
- `int next()` Moves the pointer to the right, then returns the number at the pointer.
- `boolean hasPrev()` Returns `true` if there exists a number in the traversal to the left of the pointer.
- `int prev()` Moves the pointer to the left, then returns the number at the pointer.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["BSTIterator", "next", "next", "prev", "next", "hasNext", "next", "next", "next", "hasNext", "hasPrev", "prev", "prev"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], [], [], [], []]
Output:
[null, 3, 7, 3, 7, true, 9, 15, 20, false, true, 15, 9]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next`, `prev`, `hasNext`, `hasPrev`: O(1) amortized
Space Complexity: O(N) to buffer in-order traversal nodes.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain an append-only `history: list[int]` of in-order traversed values and a cursor `pointer: int` initialized to `-1`.
Also maintain standard BST DFS stack for lazy expansion.
- `hasNext()`: returns `pointer + 1 < len(history) or len(stack) > 0`.
- `next()`: if `pointer + 1 < len(history)` advance pointer and return cached value; else pop from BST stack, expand right branch, append to history, advance pointer.
- `hasPrev()`: returns `pointer > 0`.
- `prev()`: decrement pointer and return `history[pointer]`.
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
    """Bidirectional BST Iterator supporting next() and prev() with lazy traversal."""

    def __init__(self, root: TreeNode | None) -> None:
        self.stack: list[TreeNode] = []
        self.history: list[int] = []
        self.cursor: int = -1
        self._push_left(root)

    def _push_left(self, node: TreeNode | None) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self) -> bool:
        return self.cursor + 1 < len(self.history) or len(self.stack) > 0

    def next(self) -> int:
        self.cursor += 1
        if self.cursor < len(self.history):
            return self.history[self.cursor]

        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        self.history.append(node.val)
        return node.val

    def hasPrev(self) -> bool:
        return self.cursor > 0

    def prev(self) -> int:
        self.cursor -= 1
        return self.history[self.cursor]
class TestBSTIterator(unittest.TestCase):
    def test_example_1(self) -> None:
        root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        itr = BSTIterator(root)
        self.assertEqual(itr.next(), 3)
        self.assertEqual(itr.next(), 7)
        self.assertEqual(itr.prev(), 3)
        self.assertEqual(itr.next(), 7)
        self.assertTrue(itr.hasNext())
        self.assertEqual(itr.next(), 9)
        self.assertEqual(itr.next(), 15)
        self.assertEqual(itr.next(), 20)
        self.assertFalse(itr.hasNext())
        self.assertTrue(itr.hasPrev())
        self.assertEqual(itr.prev(), 15)
        self.assertEqual(itr.prev(), 9)


if __name__ == "__main__":
    unittest.main()
