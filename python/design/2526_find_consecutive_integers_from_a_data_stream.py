"""
LeetCode 2526: Find Consecutive Integers from a Data Stream
Difficulty: Medium
Tags: Queue, Counting, Design, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
For a stream of integers, implement a data structure that checks if the last `k` integers parsed in the stream are equal to `value`.

Implement the `DataStream` class:
- `DataStream(int value, int k)` Initializes the object with `value` and `k`.
- `boolean consec(int num)` Adds `num` to the stream of integers. Returns `true` if the last `k` integers are equal to `value`, and `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["DataStream", "consec", "consec", "consec", "consec"]
[[4, 3], [4], [4], [4], [3]]
Output:
[null, false, false, true, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `consec(num)`: O(1)
Space Complexity: O(1)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain a consecutive streak counter `self.count`.
On `consec(num)`:
- If `num == self.value`: `self.count += 1`.
- Else: `self.count = 0`.
Return `self.count >= self.k` in O(1)!
"""

import unittest
class DataStream:
    """O(1) consecutive integer streak validator."""

    def __init__(self, value: int, k: int) -> None:
        self.val: int = value
        self.k: int = k
        self.streak: int = 0

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.streak += 1
        else:
            self.streak = 0
        return self.streak >= self.k

class TestDataStream(unittest.TestCase):
    def test_example_1(self) -> None:
        ds = DataStream(4, 3)
        self.assertFalse(ds.consec(4))
        self.assertFalse(ds.consec(4))
        self.assertTrue(ds.consec(4))
        self.assertFalse(ds.consec(3))


if __name__ == "__main__":
    unittest.main()
