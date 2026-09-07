"""
LeetCode 716: Max Stack
Difficulty: Hard
Tags: Linked List, Doubly-Linked List, Design, Heap (Priority Queue), Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the `MaxStack` class:
- `MaxStack()` Initializes the stack object.
- `void push(int x)` Pushes element `x` onto the stack.
- `int pop()` Removes the element on top of the stack and returns it.
- `int top()` Gets the element on the top of the stack without removing it.
- `int peekMax()` Retrieves the maximum element in the stack without removing it.
- `int popMax()` Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

Can you come up with each operation running in `O(log N)` or `O(1)`?

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output:
[null, null, null, null, 5, 5, 1, 5, 1, 5]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `push`, `pop`, `peekMax`, `popMax`: O(log N) using max-heap with lazy deletion and doubly-linked list.
- `top`: O(1)
Space Complexity: O(N) to store elements.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Doubly Linked List (for stack order) + a Max-Heap (for fast maximum retrieval).
Each node has a unique `node_id`.
Keep a `deleted: set[int]` of removed node IDs for lazy deletion:
- When `pop()` removes from stack, add node ID to `deleted`.
- When `popMax()` pops from heap, discard if ID in `deleted`, else remove node from linked list and add ID to `deleted`.
"""

import unittest
import heapq


class Node:
    def __init__(self, val: int, node_id: int) -> None:
        self.val: int = val
        self.id: int = node_id
        self.prev: Node | None = None
        self.next: Node | None = None


class MaxStack:
    """Max Stack supporting O(log N) popMax() via Doubly-Linked List and Max-Heap."""

    def __init__(self) -> None:
        self.head: Node = Node(0, -1)
        self.tail: Node = Node(0, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.heap: list[tuple[int, int, Node]] = []  # (-val, -id, node)
        self.deleted: set[int] = set()
        self.id_counter: int = 0

    def _remove_node(self, node: Node) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.deleted.add(node.id)

    def _clean_heap(self) -> None:
        while self.heap and self.heap[0][2].id in self.deleted:
            heapq.heappop(self.heap)

    def _clean_stack(self) -> None:
        while (
            self.tail.prev != self.head
            and self.tail.prev is not None
            and self.tail.prev.id in self.deleted
        ):
            self.tail.prev = self.tail.prev.prev
            if self.tail.prev:
                self.tail.prev.next = self.tail

    def push(self, x: int) -> None:
        node = Node(x, self.id_counter)
        self.id_counter += 1

        # Insert at tail (top of stack)
        prev = self.tail.prev
        assert prev is not None
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

        heapq.heappush(self.heap, (-x, -node.id, node))

    def pop(self) -> int:
        self._clean_stack()
        top_node = self.tail.prev
        assert top_node is not None and top_node != self.head
        self._remove_node(top_node)
        return top_node.val

    def top(self) -> int:
        self._clean_stack()
        assert self.tail.prev is not None and self.tail.prev != self.head
        return self.tail.prev.val

    def peekMax(self) -> int:
        self._clean_heap()
        return -self.heap[0][0]

    def popMax(self) -> int:
        self._clean_heap()
        _, _, node = heapq.heappop(self.heap)
        self._remove_node(node)
        return node.val
class TestMaxStack(unittest.TestCase):
    def test_example_1(self) -> None:
        ms = MaxStack()
        ms.push(5)
        ms.push(1)
        ms.push(5)
        self.assertEqual(ms.top(), 5)
        self.assertEqual(ms.popMax(), 5)
        self.assertEqual(ms.top(), 1)
        self.assertEqual(ms.peekMax(), 5)
        self.assertEqual(ms.pop(), 1)
        self.assertEqual(ms.top(), 5)


if __name__ == "__main__":
    unittest.main()
