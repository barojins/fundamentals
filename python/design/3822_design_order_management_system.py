"""
LeetCode 3822: Design Order Management System
Difficulty: Medium
Tags: Hash Table, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an order management system that tracks active orders and cumulative customer spending.

Implement the `OrderManagement` class:
- `OrderManagement()`
- `void placeOrder(int orderId, int customerId, int amount)`
- `bool cancelOrder(int orderId)`
- `int getCustomerTotal(int customerId)` Returns total active spending for `customerId`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["OrderManagement", "placeOrder", "placeOrder", "getCustomerTotal", "cancelOrder", "getCustomerTotal"]
[[], [1, 100, 50], [2, 100, 30], [100], [1], [100]]
Output:
[null, null, null, 80, true, 30]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `placeOrder`, `cancelOrder`, `getCustomerTotal`: O(1)
Space Complexity: O(Active orders + Customers).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `orders: dict[orderId, (customerId, amount)]`
- `customer_totals: dict[customerId, int]`
"""

import unittest
class OrderManagement:
    """E-commerce order and active customer balance management system."""

    def __init__(self) -> None:
        self.orders: dict[int, tuple[int, int]] = {}  # orderId -> (customerId, amount)
        self.customer_totals: dict[int, int] = {}

    def placeOrder(self, orderId: int, customerId: int, amount: int) -> None:
        self.orders[orderId] = (customerId, amount)
        self.customer_totals[customerId] = (
            self.customer_totals.get(customerId, 0) + amount
        )

    def cancelOrder(self, orderId: int) -> bool:
        if orderId not in self.orders:
            return False
        customerId, amount = self.orders.pop(orderId)
        self.customer_totals[customerId] -= amount
        return True

    def getCustomerTotal(self, customerId: int) -> int:
        return self.customer_totals.get(customerId, 0)
class TestOrderManagement(unittest.TestCase):
    def test_example_1(self) -> None:
        om = OrderManagement()
        om.placeOrder(1, 100, 50)
        om.placeOrder(2, 100, 30)
        self.assertEqual(om.getCustomerTotal(100), 80)
        self.assertTrue(om.cancelOrder(1))
        self.assertEqual(om.getCustomerTotal(100), 30)


if __name__ == "__main__":
    unittest.main()
