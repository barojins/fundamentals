"""
LeetCode 341: Flatten Nested List Iterator
Difficulty: Medium
Tags: Stack, Tree, Depth-First Search, Design, Queue, Iterator

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Flatten nested integer list with lazy iterator.

Implement `NestedIterator`:
- `int next()`
- `boolean hasNext()`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next`: O(1)
- `hasNext`: O(1) amortized
Space Complexity: O(D) stack depth.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Reverse stack expansion in `hasNext()`.
"""

import unittest


class NestedInteger:
    """Mock implementation of the LeetCode NestedInteger interface."""

    def __init__(self, val_or_list: int | list["NestedInteger"]) -> None:
        if isinstance(val_or_list, int):
            self._integer: int | None = val_or_list
            self._list: list[NestedInteger] | None = None
        else:
            self._integer = None
            self._list = val_or_list

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int | None:
        return self._integer

    def getList(self) -> list["NestedInteger"] | None:
        return self._list


class NestedIterator:
    """Lazy iterator that flattens a nested list using a stack."""

    def __init__(self, nestedList: list[NestedInteger]) -> None:
        self.stack: list[NestedInteger] = list(reversed(nestedList))

    def next(self) -> int:
        return self.stack.pop().getInteger()  # type: ignore

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            nested_list = top.getList()
            if nested_list:
                for item in reversed(nested_list):
                    self.stack.append(item)
        return False


class TestNestedIterator(unittest.TestCase):
    def test_example_1(self) -> None:
        nested = [
            NestedInteger([NestedInteger(1), NestedInteger(1)]),
            NestedInteger(2),
            NestedInteger([NestedInteger(1), NestedInteger(1)]),
        ]
        iterator = NestedIterator(nested)
        res = []
        while iterator.hasNext():
            res.append(iterator.next())
        self.assertEqual(res, [1, 1, 2, 1, 1])


if __name__ == "__main__":
    unittest.main()
