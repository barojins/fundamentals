"""
LeetCode 297: Serialize and Deserialize Binary Tree
Difficulty: Hard
Tags: String, Tree, Depth-First Search, Breadth-First Search, Binary Tree, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an algorithm to serialize and deserialize a binary tree.

Implement `Codec`:
- `String serialize(TreeNode root)`
- `TreeNode deserialize(String data)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `serialize`, `deserialize`: O(N)
Space Complexity: O(N)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Pre-order DFS with null delimiters `#` and comma separation.
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


class Codec:
    """Serializes and deserializes a binary tree using pre-order DFS."""

    def serialize(self, root: TreeNode | None) -> str:
        tokens: list[str] = []

        def dfs(node: TreeNode | None) -> None:
            if not node:
                tokens.append("#")
                return
            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data: str) -> TreeNode | None:
        tokens = iter(data.split(","))

        def dfs() -> TreeNode | None:
            val = next(tokens)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


class TestCodec(unittest.TestCase):
    def test_example_1(self) -> None:
        codec = Codec()
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        s = codec.serialize(root)
        recovered = codec.deserialize(s)
        self.assertEqual(codec.serialize(recovered), s)

    def test_empty_tree(self) -> None:
        codec = Codec()
        self.assertIsNone(codec.deserialize(codec.serialize(None)))


if __name__ == "__main__":
    unittest.main()
