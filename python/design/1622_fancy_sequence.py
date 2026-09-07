"""
LeetCode 1622: Fancy Sequence
Difficulty: Hard
Tags: Math, Design, Segment Tree

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the `Fancy` class:
- `Fancy()` Initializes the object with an empty sequence.
- `void append(int val)` Appends an integer `val` to the end of the sequence.
- `void addAll(int inc)` Increments all existing values in the sequence by an integer `inc`.
- `void multAll(int m)` Multiplies all existing values in the sequence by an integer `m`.
- `int getIndex(int idx)` Gets the current value at index `idx` (0-indexed) of the sequence modulo `10^9 + 7`. If the index is greater or equal than the length of the sequence, return `-1`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output:
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `append`, `addAll`, `multAll`: O(1) using global linear transformation state (a * x + b).
- `getIndex`: O(1) (with modular inverse)
Space Complexity: O(N) to store normalized initial values.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain global linear transformation parameters `a = 1`, `b = 0` representing `current_val = a * x + b (mod MOD)`.
- `addAll(inc)`: `b = (b + inc) % MOD`.
- `multAll(m)`: `a = (a * m) % MOD`, `b = (b * m) % MOD`.
- `append(val)`: store transformed initial value `x = (val - b) * pow(a, MOD - 2, MOD) % MOD`.
- `getIndex(idx)`: return `(a * stored_x[idx] + b) % MOD` in O(1)!
"""

import unittest
class Fancy:
    """O(1) Sequence modifications using global linear modular transforms."""

    MOD = 1_000_000_007

    def __init__(self) -> None:
        self.vals: list[int] = []
        self.a: int = 1
        self.b: int = 0

    def append(self, val: int) -> None:
        # Inverse transform: x = (val - b) / a  (mod MOD)
        inv_a = pow(self.a, self.MOD - 2, self.MOD)
        normalized = ((val - self.b) % self.MOD * inv_a) % self.MOD
        self.vals.append(normalized)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        return (self.a * self.vals[idx] + self.b) % self.MOD
class TestFancy(unittest.TestCase):
    def test_example_1(self) -> None:
        fancy = Fancy()
        fancy.append(2)
        fancy.addAll(3)
        fancy.append(7)
        fancy.multAll(2)
        self.assertEqual(fancy.getIndex(0), 10)
        fancy.addAll(3)
        fancy.append(10)
        fancy.multAll(2)
        self.assertEqual(fancy.getIndex(0), 26)
        self.assertEqual(fancy.getIndex(1), 34)
        self.assertEqual(fancy.getIndex(2), 20)


if __name__ == "__main__":
    unittest.main()
