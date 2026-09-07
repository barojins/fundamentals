"""
LeetCode 1261: Find Elements in a Contaminated Binary Tree
Difficulty: Medium
Tags: Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given a binary tree with the rule `root.val == 0`, and any node with value `x`:
- If `node.left` exists, `node.left.val == 2 * x + 1`.
- If `node.right` exists, `node.right.val == 2 * x + 2`.

Now the tree is contaminated, which means all `Node.val` have been changed to `-1`.

Implement the `FindElements` class:
- `FindElements(TreeNode* root)` Initializes the object with a contaminated binary tree and recovers it.
- `bool find(int target)` Returns `true` if the `target` value exists in the recovered binary tree.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output:
[null,false,true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N) DFS/BFS recovery.
- `find(target)`: O(1) hash set lookup.
Space Complexity: O(N) to store values in a set.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Traverse the tree recursively from root starting with value `0`.
For each node with recovered value `x`:
- Add `x` to a `values: set[int]`.
- Recurse on `node.left` with value `2 * x + 1`.
- Recurse on `node.right` with value `2 * x + 2`.
`find(target)` simply does `target in self.values` in O(1) time.
"""

import unittest
class TreeNode:
    def __init__(
        self,
        val: int = -1,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class FindElements:
    """Recovers a contaminated binary tree and provides O(1) value lookup."""

    def __init__(self, root: TreeNode | None) -> None:
        self.values: set[int] = set()

        def recover(node: TreeNode | None, val: int) -> None:
            if not node:
                return
            node.val = val
            self.values.add(val)
            if node.left:
                recover(node.left, 2 * val + 1)
            if node.right:
                recover(node.right, 2 * val + 2)

        if root:
            recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

class TestFindElements(unittest.TestCase):
    def test_example_1(self) -> None:
        root = TreeNode(-1, None, TreeNode(-1))
        fe = FindElements(root)
        self.assertFalse(fe.find(1))
        self.assertTrue(fe.find(2))

    def test_full_tree(self) -> None:
        root = TreeNode(-1, TreeNode(-1, TreeNode(-1), TreeNode(-1)), TreeNode(-1))
        fe = FindElements(root)
        self.assertTrue(fe.find(0))
        self.assertTrue(fe.find(1))
        self.assertTrue(fe.find(2))
        self.assertTrue(fe.find(3))
        self.assertTrue(fe.find(4))
        self.assertFalse(fe.find(100))


if __name__ == "__main__":
    unittest.main()
