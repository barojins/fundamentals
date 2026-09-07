"""
LeetCode 1357: Apply Discount Every n Orders
Difficulty: Medium
Tags: Array, Hash Table, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
There is a supermarket that is offering a discount on all items for every `n-th` customer.

Implement the `Cashier` class:
- `Cashier(int n, int discount, int[] products, int[] prices)` Initializes the object with `n`, the discount percentage `discount`, and the `products` and their `prices`.
- `double getBill(int[] product, int[] amount)` Computes the total bill for customer items, applying discount `total - (discount * total) / 100` if the customer is the `n-th` customer since the last discount.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[7,5,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,99,10,10,10]],[[2,3,5],[5,3,2]]]
Output:
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `getBill`: O(number of items purchased)
Space Complexity: O(P) to store product prices.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map product IDs to prices: `product_prices: dict[int, int]`.
Track customer count `self.customer_count += 1`.
If `self.customer_count % n == 0`, apply discount `total * ((100 - discount) / 100)`.
"""

import unittest
class Cashier:
    """Supermarket checkout register applying discount to every n-th customer."""

    def __init__(
        self, n: int, discount: int, products: list[int], prices: list[int]
    ) -> None:
        self.n: int = n
        self.discount: int = discount
        self.prices: dict[int, int] = dict(zip(products, prices))
        self.customer_count: int = 0

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.customer_count += 1
        total = 0.0
        for p, a in zip(product, amount):
            total += self.prices[p] * a

        if self.customer_count % self.n == 0:
            total = total * (1.0 - self.discount / 100.0)

        return total
class TestCashier(unittest.TestCase):
    def test_example_1(self) -> None:
        cashier = Cashier(
        7, 5, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100]
        )
        self.assertEqual(cashier.getBill([1, 2], [1, 2]), 500.0)
        self.assertEqual(cashier.getBill([3, 7], [10, 10]), 4000.0)


if __name__ == "__main__":
    unittest.main()
