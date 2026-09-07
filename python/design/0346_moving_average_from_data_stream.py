"""
LeetCode 346: Moving Average from Data Stream
Difficulty: Easy
Tags: Array, Design, Queue, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the `MovingAverage` class:
- `MovingAverage(int size)` Initializes the object with the size of the window `size`.
- `double next(int val)` Returns the moving average of the last `size` values of the stream.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output:
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation:
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next(val)`: O(1)
Space Complexity: O(size) for the circular queue / sliding window.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a `collections.deque` of maximum capacity `size` and maintain a running sum `self.window_sum`.
On `next(val)`:
- If queue is at capacity, `self.window_sum -= queue.popleft()`.
- `queue.append(val)` and `self.window_sum += val`.
- Return `self.window_sum / len(queue)`.
"""

from collections import deque
import unittest


class MovingAverage:
    """Calculates moving average over a sliding window of fixed size."""

    def __init__(self, size: int) -> None:
        self.size: int = size
        self.queue: deque[int] = deque()
        self.window_sum: int = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.window_sum -= self.queue.popleft()
        self.queue.append(val)
        self.window_sum += val
        return self.window_sum / len(self.queue)


class TestMovingAverage(unittest.TestCase):
    def test_example_1(self) -> None:
        ma = MovingAverage(3)
        self.assertAlmostEqual(ma.next(1), 1.0, places=5)
        self.assertAlmostEqual(ma.next(10), 5.5, places=5)
        self.assertAlmostEqual(ma.next(3), 14 / 3, places=5)
        self.assertAlmostEqual(ma.next(5), 6.0, places=5)

    def test_window_size_one(self) -> None:
        ma = MovingAverage(1)
        self.assertAlmostEqual(ma.next(10), 10.0)
        self.assertAlmostEqual(ma.next(-5), -5.0)
        self.assertAlmostEqual(ma.next(100), 100.0)

    def test_negative_values(self) -> None:
        ma = MovingAverage(2)
        self.assertAlmostEqual(ma.next(-1), -1.0)
        self.assertAlmostEqual(ma.next(-3), -2.0)
        self.assertAlmostEqual(ma.next(5), 1.0)


if __name__ == "__main__":
    unittest.main()
