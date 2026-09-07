"""
LeetCode 622: Design Circular Queue
Difficulty: Medium
Tags: Array, Linked List, Design, Queue

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

Implement the `MyCircularQueue` class:
- `MyCircularQueue(k)` Initializes the object with the size of the queue to be `k`.
- `int Front()` Gets the front item from the queue. If the queue is empty, return `-1`.
- `int Rear()` Gets the last item from the queue. If the queue is empty, return `-1`.
- `boolean enQueue(int value)` Inserts an element into the circular queue. Return `true` if the operation is successful.
- `boolean deQueue()` Deletes an element from the circular queue. Return `true` if the operation is successful.
- `boolean isEmpty()` Checks whether the circular queue is empty or not.
- `boolean isFull()` Checks whether the circular queue is full or not.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output:
[null, true, true, true, false, 3, true, true, true, 4]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- All operations (`enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, `isFull`): O(1)
Space Complexity: O(k) for fixed size array.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a fixed size array `queue = [0] * k` with `head = 0`, `size = 0`, `capacity = k`.
- `enQueue(val)`: `queue[(head + size) % capacity] = val; size += 1`
- `deQueue()`: `head = (head + 1) % capacity; size -= 1`
- `Front()`: `queue[head]`
- `Rear()`: `queue[(head + size - 1) % capacity]`
"""

import unittest
class MyCircularQueue:
    """Ring buffer / Circular Queue implemented with a fixed-size array."""

    def __init__(self, k: int) -> None:
        self.capacity: int = k
        self.queue: list[int] = [0] * k
        self.head: int = 0
        self.size: int = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        tail_idx = (self.head + self.size) % self.capacity
        self.queue[tail_idx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        tail_idx = (self.head + self.size - 1) % self.capacity
        return self.queue[tail_idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
class TestMyCircularQueue(unittest.TestCase):
    def test_example_1(self) -> None:
        cq = MyCircularQueue(3)
        self.assertTrue(cq.enQueue(1))
        self.assertTrue(cq.enQueue(2))
        self.assertTrue(cq.enQueue(3))
        self.assertFalse(cq.enQueue(4))
        self.assertEqual(cq.Rear(), 3)
        self.assertTrue(cq.isFull())
        self.assertTrue(cq.deQueue())
        self.assertTrue(cq.enQueue(4))
        self.assertEqual(cq.Rear(), 4)


if __name__ == "__main__":
    unittest.main()
