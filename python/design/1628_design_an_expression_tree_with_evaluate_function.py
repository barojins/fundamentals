"""
LeetCode 1628: Design an Expression Tree With Evaluate Function
Difficulty: Medium
Tags: Math, Stack, Tree, Design, Binary Tree

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given the postfix tokens of an arithmetic expression, build and return the expression tree that represents this expression.

An expression tree is a binary tree where each leaf is an operand (a non-negative integer) and each non-leaf is an operator (`+`, `-`, `*`, or `/`).

The evaluate function should return the value of the expression tree represented by the root node.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: s = ["3","4","+","2","*","7","/"]
Output: 2
Explanation: this expression evaluates to ((3+4)*2)/7 = 14/7 = 2.

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `buildTree`: O(N) using stack over postfix tokens.
- `evaluate`: O(N) post-order tree evaluation.
Space Complexity: O(N) to store tree nodes.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use an abstract syntax tree:
Each `Node` has `val: str`, `left: Node | None`, `right: Node | None`.
- Leaf nodes return `int(self.val)`.
- Operator nodes recursively evaluate `left` and `right` and apply the operator with integer division `//`.
"""

import unittest
from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class ExpressionNode(Node):
    def __init__(
        self,
        val: str,
        left: "ExpressionNode | None" = None,
        right: "ExpressionNode | None" = None,
    ) -> None:
        self.val: str = val
        self.left: ExpressionNode | None = left
        self.right: ExpressionNode | None = right

    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)

        assert self.left is not None and self.right is not None
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.val == "+":
            return left_val + right_val
        elif self.val == "-":
            return left_val - right_val
        elif self.val == "*":
            return left_val * right_val
        elif self.val == "/":
            return left_val // right_val
        raise ValueError(f"Unknown operator {self.val}")


class TreeBuilder:
    """Builds an expression tree from postfix notation tokens."""

    def buildTree(self, postfix: list[str]) -> Node:
        stack: list[ExpressionNode] = []
        for token in postfix:
            if token in {"+", "-", "*", "/"}:
                right = stack.pop()
                left = stack.pop()
                stack.append(ExpressionNode(token, left, right))
            else:
                stack.append(ExpressionNode(token))
        return stack[-1]

class TestTreeBuilder(unittest.TestCase):
    def test_example_1(self) -> None:
        builder = TreeBuilder()
        tree = builder.buildTree(["3", "4", "+", "2", "*", "7", "/"])
        self.assertEqual(tree.evaluate(), 2)

    def test_simple_expression(self) -> None:
        builder = TreeBuilder()
        tree = builder.buildTree(["4", "5", "2", "-", "*"])
        self.assertEqual(tree.evaluate(), 12)


if __name__ == "__main__":
    unittest.main()
