"""
LeetCode 895: Maximum Frequency Stack
Difficulty: Hard
Tags: Hash Table, Stack, Design, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the `FreqStack` class:
- `FreqStack()` constructs an empty frequency stack.
- `void push(int val)` pushes an integer `val` onto the top of the stack.
- `int pop()` removes and returns the most frequent element in the stack.
  - If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output:
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation:
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `push`: O(1)
- `pop`: O(1)
Space Complexity: O(N) where N is number of elements in the stack.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `freq: Counter[int]` tracking frequency of each element.
- `group: dict[int, list[int]]` mapping each frequency level to a stack of elements with at least that frequency.
- `max_freq: int` tracking current maximum frequency.
On `push(x)`: increment `freq[x]`, push `x` to `group[freq[x]]`, update `max_freq`.
On `pop()`: pop top from `group[max_freq]`, decrement `freq[x]`. If `group[max_freq]` is empty, decrement `max_freq`.
"""

import unittest
from collections import Counter, defaultdict


class FreqStack:
    """O(1) Maximum Frequency Stack using frequency-level bucketed stacks."""

    def __init__(self) -> None:
        self.freq: Counter[int] = Counter()
        self.group: dict[int, list[int]] = defaultdict(list)
        self.max_freq: int = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val

class TestFreqStack(unittest.TestCase):
    def test_example_1(self) -> None:
        fs = FreqStack()
        for x in [5, 7, 5, 7, 4, 5]:
            fs.push(x)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 7)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 4)

    def test_empty_and_single(self) -> None:
        fs = FreqStack()
        fs.push(1)
        self.assertEqual(fs.pop(), 1)


if __name__ == "__main__":
    unittest.main()
