"""
LeetCode 2034: Stock Price Fluctuation
Difficulty: Medium
Tags: Hash Table, Design, Heap (Priority Queue), Ordered Set, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Implement the `StockPrice` class:
- `StockPrice()` Initializes the object with no price records.
- `void update(int timestamp, int price)` Updates the price of the stock at the given timestamp.
- `int current()` Returns the latest price of the stock.
- `int maximum()` Returns the maximum price of the stock.
- `int minimum()` Returns the minimum price of the stock.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output:
[null, null, null, 5, 10, null, 5, null, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `update`: O(log N)
- `current`: O(1)
- `maximum`, `minimum`: O(1) amortized lazy heap cleanup.
Space Complexity: O(N) for history map and min/max heaps.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `prices: dict[timestamp, price]`
- `max_timestamp: int`
- `max_heap: list[(-price, timestamp)]`
- `min_heap: list[(price, timestamp)]`
Lazy deletion on `maximum()` and `minimum()`:
While top of heap has a price != current recorded `prices[timestamp]`, pop it off!
"""

import unittest
import heapq


class StockPrice:
    """Stock price tracker with O(log N) updates and O(1) amortized min/max/current queries."""

    def __init__(self) -> None:
        self.prices: dict[int, int] = {}
        self.latest_timestamp: int = 0
        self.max_heap: list[tuple[int, int]] = []  # (-price, timestamp)
        self.min_heap: list[tuple[int, int]] = []  # (price, timestamp)

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        if timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp

        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest_timestamp]

    def maximum(self) -> int:
        while self.max_heap:
            neg_p, t = self.max_heap[0]
            if self.prices[t] == -neg_p:
                return -neg_p
            heapq.heappop(self.max_heap)
        return -1

    def minimum(self) -> int:
        while self.min_heap:
            p, t = self.min_heap[0]
            if self.prices[t] == p:
                return p
            heapq.heappop(self.min_heap)
        return -1
class TestStockPrice(unittest.TestCase):
    def test_example_1(self) -> None:
        sp = StockPrice()
        sp.update(1, 10)
        sp.update(2, 5)
        self.assertEqual(sp.current(), 5)
        self.assertEqual(sp.maximum(), 10)
        sp.update(1, 3)
        self.assertEqual(sp.maximum(), 5)
        sp.update(4, 2)
        self.assertEqual(sp.minimum(), 2)


if __name__ == "__main__":
    unittest.main()
