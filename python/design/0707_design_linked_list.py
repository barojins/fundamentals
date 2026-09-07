"""
LeetCode 707: Design Linked List
Difficulty: Medium
Tags: Linked List, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the current node, and `next` is a pointer/reference to the next node.

Implement the `MyLinkedList` class:
- `MyLinkedList()` Initializes the `MyLinkedList` object.
- `int get(int index)` Get the value of the `indexth` node in the linked list. If the index is invalid, return `-1`.
- `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list.
- `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.
- `void addAtIndex(int index, int val)` Add a node of value `val` before the `indexth` node in the linked list. If `index == length`, append to end. If `index > length`, do not insert.
- `void deleteAtIndex(int index)` Delete the `indexth` node in the linked list, if the index is valid.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output:
[null, null, null, null, 2, null, 3]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addAtHead`, `addAtTail`: O(1) with doubly linked list.
- `get`, `addAtIndex`, `deleteAtIndex`: O(index)
Space Complexity: O(N) to store nodes.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Doubly Linked List with dummy `head` and `tail` sentinels.
Maintain `size: int` so boundary checks `0 <= index < size` can be done in O(1).
Traverse from `head` or `tail` depending on whether `index < size // 2` for speed.
"""

import unittest
class DLNode:
    def __init__(self, val: int = 0) -> None:
        self.val: int = val
        self.prev: DLNode | None = None
        self.next: DLNode | None = None


class MyLinkedList:
    """Doubly-linked list implementation with head and tail sentinels."""

    def __init__(self) -> None:
        self.head: DLNode = DLNode()
        self.tail: DLNode = DLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size: int = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            assert curr is not None
            curr = curr.next
        assert curr is not None
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        pred = self.head
        for _ in range(index):
            assert pred.next is not None
            pred = pred.next

        succ = pred.next
        new_node = DLNode(val)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        if succ:
            succ.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        pred = self.head
        for _ in range(index):
            assert pred.next is not None
            pred = pred.next

        to_delete = pred.next
        assert to_delete is not None
        succ = to_delete.next
        pred.next = succ
        if succ:
            succ.prev = pred

        self.size -= 1
class TestMyLinkedList(unittest.TestCase):
    def test_example_1(self) -> None:
        ll = MyLinkedList()
        ll.addAtHead(1)
        ll.addAtTail(3)
        ll.addAtIndex(1, 2)
        self.assertEqual(ll.get(1), 2)
        ll.deleteAtIndex(1)
        self.assertEqual(ll.get(1), 3)


if __name__ == "__main__":
    unittest.main()
