"""
LeetCode 641: Design Circular Deque
Difficulty: Medium
Tags: Array, Linked List, Design, Queue

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design your implementation of the circular double-ended queue (deque).

Implement the `MyCircularDeque` class:
- `MyCircularDeque(int k)` Initializes the deque with a maximum size of `k`.
- `boolean insertFront()` Adds an item at the front of Deque. Indicates if the operation was successful.
- `boolean insertLast()` Adds an item at the rear of Deque. Indicates if the operation was successful.
- `boolean deleteFront()` Deletes an item from the front of Deque. Indicates if the operation was successful.
- `boolean deleteLast()` Deletes an item from the rear of Deque. Indicates if the operation was successful.
- `int getFront()` Returns the front item from the Deque. If the deque is empty, returns `-1`.
- `int getRear()` Returns the last item from Deque. If the deque is empty, returns `-1`.
- `boolean isEmpty()` Returns `true` if the deque is empty, or `false` otherwise.
- `boolean isFull()` Returns `true` if the deque is full, or `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output:
[null, true, true, true, false, 2, true, true, true, 4]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- All operations: O(1)
Space Complexity: O(k) for circular array storage.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use an array `deque = [0] * k` with `front = 0`, `size = 0`, `capacity = k`.
- `insertFront(val)`: `front = (front - 1 + k) % k; deque[front] = val; size += 1`
- `insertLast(val)`: `deque[(front + size) % k] = val; size += 1`
- `deleteFront()`: `front = (front + 1) % k; size -= 1`
- `deleteLast()`: `size -= 1`
- `getFront()`: `deque[front]`
- `getRear()`: `deque[(front + size - 1) % k]`
"""

import unittest
class MyCircularDeque:
    """Circular double-ended queue (deque) with O(1) operations."""

    def __init__(self, k: int) -> None:
        self.capacity: int = k
        self.queue: list[int] = [0] * k
        self.front: int = 0
        self.size: int = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        idx = (self.front + self.size) % self.capacity
        self.queue[idx] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        idx = (self.front + self.size - 1) % self.capacity
        return self.queue[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
class TestMyCircularDeque(unittest.TestCase):
    def test_example_1(self) -> None:
        cd = MyCircularDeque(3)
        self.assertTrue(cd.insertLast(1))
        self.assertTrue(cd.insertLast(2))
        self.assertTrue(cd.insertFront(3))
        self.assertFalse(cd.insertFront(4))
        self.assertEqual(cd.getRear(), 2)
        self.assertTrue(cd.isFull())
        self.assertTrue(cd.deleteLast())
        self.assertTrue(cd.insertFront(4))
        self.assertEqual(cd.getFront(), 4)


if __name__ == "__main__":
    unittest.main()
