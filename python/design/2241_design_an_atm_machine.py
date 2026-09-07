"""
LeetCode 2241: Design an ATM Machine
Difficulty: Medium
Tags: Array, Greedy, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
There is an ATM machine that stores bank notes of 5 denominations: 20, 50, 100, 200, and 500 dollars. Initially the ATM is empty.

Implement the `ATM` class:
- `ATM()` Initializes the ATM object.
- `void deposit(int[] banknotesCount)` Deposits banknotes with counts for `[20, 50, 100, 200, 500]`.
- `int[] withdraw(int amount)` Withdraws `amount` using greedy selection from highest to lowest denomination. Returns array of 5 integers representing banknotes used, or `[-1]` if cannot dispense.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]
[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]
Output:
[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `deposit`: O(1)
- `withdraw`: O(1) (fixed 5 denominations)
Space Complexity: O(1)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Denominations: `[20, 50, 100, 200, 500]`.
On `withdraw(amount)`:
Greedily take `take = min(available[i], rem // denom[i])` starting from index 4 down to 0.
If `rem == 0`: deduct taken notes and return dispensing breakdown; else return `[-1]`.
"""

import unittest
class ATM:
    """ATM banknote deposit and greedy withdrawal dispenser."""

    DENOMS = [20, 50, 100, 200, 500]

    def __init__(self) -> None:
        self.banknotes: list[int] = [0] * 5

    def deposit(self, banknotesCount: list[int]) -> None:
        for i in range(5):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> list[int]:
        used = [0] * 5
        rem = amount

        for i in range(4, -1, -1):
            denom = self.DENOMS[i]
            count = min(self.banknotes[i], rem // denom)
            used[i] = count
            rem -= count * denom

        if rem == 0:
            for i in range(5):
                self.banknotes[i] -= used[i]
            return used
        return [-1]
class TestATM(unittest.TestCase):
    def test_example_1(self) -> None:
        atm = ATM()
        atm.deposit([0, 0, 1, 2, 1])
        self.assertEqual(atm.withdraw(600), [0, 0, 1, 0, 1])
        atm.deposit([0, 1, 0, 1, 1])
        self.assertEqual(atm.withdraw(600), [-1])
        self.assertEqual(atm.withdraw(550), [0, 1, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()
