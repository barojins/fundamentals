"""
LeetCode 1472: Design Browser History
Difficulty: Medium
Tags: Array, Linked List, Stack, Design, Doubly-Linked List, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You have a browser of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:
- `BrowserHistory(string homepage)` Initializes the object with the `homepage` of the browser.
- `void visit(string url)` Visits `url` from the current page. It clears up all the forward history.
- `string back(int steps)` Move `steps` back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history at most `steps`.
- `string forward(int steps)` Move `steps` forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history at most `steps`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `visit`, `back`, `forward`: O(1)
Space Complexity: O(N) where N is number of visited URLs.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a dynamic array `history: list[str]` and two pointers: `curr` and `bound` (valid history limit).
- `visit(url)`: `curr += 1`, set `history[curr] = url` (or append), update `bound = curr`.
- `back(steps)`: `curr = max(0, curr - steps)`, return `history[curr]`.
- `forward(steps)`: `curr = min(bound, curr + steps)`, return `history[curr]`.
"""

import unittest
class BrowserHistory:
    """Browser navigation history with O(1) back and forward jumps."""

    def __init__(self, homepage: str) -> None:
        self.history: list[str] = [homepage]
        self.curr: int = 0
        self.bound: int = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr < len(self.history):
            self.history[self.curr] = url
        else:
            self.history.append(url)
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.bound, self.curr + steps)
        return self.history[self.curr]
class TestBrowserHistory(unittest.TestCase):
    def test_example_1(self) -> None:
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.visit("youtube.com")
        self.assertEqual(bh.back(1), "facebook.com")
        self.assertEqual(bh.back(1), "google.com")
        self.assertEqual(bh.forward(1), "facebook.com")
        bh.visit("linkedin.com")
        self.assertEqual(bh.forward(2), "linkedin.com")
        self.assertEqual(bh.back(2), "google.com")
        self.assertEqual(bh.back(7), "leetcode.com")


if __name__ == "__main__":
    unittest.main()
