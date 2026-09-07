"""
LeetCode 2166: Design Bitset
Difficulty: Medium
Tags: Array, Hash Table, Design, Bit Manipulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A Bitset is a data structure that compacts bits.

Implement the `Bitset` class:
- `Bitset(int size)` Initializes the Bitset with `size` bits, all initially `0`.
- `void fix(int idx)` Updates the value of the bit at index `idx` to `1`.
- `void unfix(int idx)` Updates the value of the bit at index `idx` to `0`.
- `void flip()` Flips the values of all the bits in the Bitset.
- `boolean all()` Checks if the value of each bit in the Bitset is `1`.
- `boolean one()` Checks if there is at least one bit in the Bitset with value `1`.
- `int count()` Returns the total number of bits in the Bitset which have value `1`.
- `String toString()` Returns the current composition of the Bitset.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]
Output:
[null, null, null, null, false, null, null, true, null, 2, "01010"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- All operations except `toString`: O(1)
- `toString`: O(N)
Space Complexity: O(N) for bit array.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `bits: list[int]`
- `flipped: bool` (tracks whether logical bits are inverted)
- `ones_count: int`
On `flip()`: `flipped = not flipped`, `ones_count = size - ones_count` in O(1)!
"""

import unittest
class Bitset:
    """O(1) Bitset supporting instant lazy flips."""

    def __init__(self, size: int) -> None:
        self.size: int = size
        self.bits: list[int] = [0] * size
        self.flipped: bool = False
        self.ones_count: int = 0

    def fix(self, idx: int) -> None:
        val = 0 if self.flipped else 1
        if self.bits[idx] != val:
            self.bits[idx] = val
            self.ones_count += 1

    def unfix(self, idx: int) -> None:
        val = 1 if self.flipped else 0
        if self.bits[idx] != val:
            self.bits[idx] = val
            self.ones_count -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones_count = self.size - self.ones_count

    def all(self) -> bool:
        return self.ones_count == self.size

    def one(self) -> bool:
        return self.ones_count > 0

    def count(self) -> int:
        return self.ones_count

    def toString(self) -> str:
        if not self.flipped:
            return "".join(str(b) for b in self.bits)
        return "".join("1" if b == 0 else "0" for b in self.bits)
class TestBitset(unittest.TestCase):
    def test_example_1(self) -> None:
        bs = Bitset(5)
        bs.fix(3)
        bs.fix(1)
        bs.flip()
        self.assertFalse(bs.all())
        bs.unfix(0)
        bs.flip()
        self.assertTrue(bs.one())
        bs.unfix(0)
        self.assertEqual(bs.count(), 2)
        self.assertEqual(bs.toString(), "01010")


if __name__ == "__main__":
    unittest.main()
