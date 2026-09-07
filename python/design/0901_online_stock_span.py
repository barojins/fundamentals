"""
LeetCode 901: Online Stock Span
Difficulty: Medium
Tags: Stack, Design, Monotonic Stack, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an algorithm that collects daily price quotes for some stock and returns the span of that day's price.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

Implement the `StockSpanner` class:
- `StockSpanner()` Initializes the object of the class.
- `int next(int price)` Returns the span of the stock's price given that today's price is `price`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output:
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation:
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were <= 75.
stockSpanner.next(85);  // return 6

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next(price)`: O(1) amortized using monotonic stack.
Space Complexity: O(N) to store stack entries.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a monotonic decreasing stack storing pairs `(price, span)`.
When a new `price` arrives:
- Initialize `span = 1`.
- While stack is non-empty and `stack[-1][0] <= price`:
  - `span += stack.pop()[1]`.
- Push `(price, span)` onto stack and return `span`.
"""

import unittest
class StockSpanner:
    """Monotonic stack online stock span calculator."""

    def __init__(self) -> None:
        # Stack elements: (price, span)
        self.stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
class TestStockSpanner(unittest.TestCase):
    def test_example_1(self) -> None:
        spanner = StockSpanner()
        self.assertEqual(spanner.next(100), 1)
        self.assertEqual(spanner.next(80), 1)
        self.assertEqual(spanner.next(60), 1)
        self.assertEqual(spanner.next(70), 2)
        self.assertEqual(spanner.next(60), 1)
        self.assertEqual(spanner.next(75), 4)
        self.assertEqual(spanner.next(85), 6)


if __name__ == "__main__":
    unittest.main()
