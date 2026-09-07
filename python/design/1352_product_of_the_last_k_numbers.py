"""
LeetCode 1352: Product of the Last K Numbers
Difficulty: Medium
Tags: Array, Math, Design, Data Stream, Prefix Sum

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an algorithm that accepts a stream of integers and retrieves the product of the last `k` integers of the stream.

Implement the `ProductOfNumbers` class:
- `ProductOfNumbers()` Initializes the object with an empty stream.
- `void add(int num)` Appends the integer `num` to the stream.
- `int getProduct(int k)` Returns the product of the last `k` numbers in the current list. You can assume that always the current list has at least `k` numbers.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
Output:
[null,null,null,null,null,null,20,40,0,null,32]

Explanation:
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20 (5 * 4)
productOfNumbers.getProduct(3); // return 40 (2 * 5 * 4)
productOfNumbers.getProduct(4); // return 0 (0 * 2 * 5 * 4)
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32 (4 * 8)

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add(num)`: O(1)
- `getProduct(k)`: O(1)
Space Complexity: O(N) for prefix product array.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain running prefix products `prefix = [1]`.
- When `num > 0`: `prefix.append(prefix[-1] * num)`.
- When `num == 0`: reset `prefix = [1]` (any query spanning across 0 will return 0).
- For `getProduct(k)`:
  - If `k >= len(prefix)`: return 0 (spans over a zero).
  - Else: return `prefix[-1] // prefix[-1 - k]`.
"""

import unittest
class ProductOfNumbers:
    """O(1) prefix products data stream supporting zero-resetting."""

    def __init__(self) -> None:
        self.prefix: list[int] = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]
class TestProductOfNumbers(unittest.TestCase):
    def test_example_1(self) -> None:
        pon = ProductOfNumbers()
        pon.add(3)
        pon.add(0)
        pon.add(2)
        pon.add(5)
        pon.add(4)
        self.assertEqual(pon.getProduct(2), 20)
        self.assertEqual(pon.getProduct(3), 40)
        self.assertEqual(pon.getProduct(4), 0)
        pon.add(8)
        self.assertEqual(pon.getProduct(2), 32)


if __name__ == "__main__":
    unittest.main()
