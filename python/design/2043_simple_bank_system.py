"""
LeetCode 2043: Simple Bank System
Difficulty: Medium
Tags: Array, Hash Table, Design, Simulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You have been tasked with writing a program for a popular bank that will automate all its operations. The bank has `n` accounts numbered from `1` to `n`. The initial balance of each account is stored in a 0-indexed integer array `balance` where the `(i + 1)-th` account has an initial balance of `balance[i]`.

Implement the `Bank` class:
- `Bank(long[] balance)` Initializes the object with the 0-indexed integer array `balance`.
- `boolean transfer(int account1, int account2, long money)` Transfers `money` from `account1` to `account2`. Returns `true` if valid, `false` otherwise.
- `boolean deposit(int account, long money)` Deposits `money` into `account`. Returns `true` if valid, `false` otherwise.
- `boolean withdraw(int account, long money)` Withdraws `money` from `account`. Returns `true` if valid, `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
Output:
[null, true, true, true, false, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `transfer`, `deposit`, `withdraw`: O(1)
Space Complexity: O(N) for balance array.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Verify:
- `1 <= account <= N`
- Sufficient balance for withdrawals and transfers.
"""

import unittest
class Bank:
    """Simple banking ledger system."""

    def __init__(self, balance: list[int]) -> None:
        self.balance: list[int] = list(balance)
        self.n: int = len(balance)

    def _valid(self, acc: int) -> bool:
        return 1 <= acc <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self._valid(account1) and self._valid(account2)):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
class TestBank(unittest.TestCase):
    def test_example_1(self) -> None:
        bank = Bank([10, 100, 20, 50, 30])
        self.assertTrue(bank.withdraw(3, 10))
        self.assertTrue(bank.transfer(5, 1, 20))
        self.assertTrue(bank.deposit(5, 20))
        self.assertFalse(bank.transfer(3, 4, 15))
        self.assertFalse(bank.withdraw(10, 50))


if __name__ == "__main__":
    unittest.main()
