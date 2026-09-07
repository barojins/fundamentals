"""
LeetCode 900: RLE Iterator
Difficulty: Medium
Tags: Array, Design, Counting, Iterator

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded sequence of even length `encoding` (0-indexed), for all even `i`, `encoding[i]` tells us the number of times that the non-negative integer value `encoding[i + 1]` is repeated in the sequence.

Implement the `RLEIterator` class:
- `RLEIterator(int[] encoding)` Initializes the object with the encoded array `encoding`.
- `int next(int n)` Exhausts the next `n` elements and returns the last element exhausted in this way. If there are no elements left to exhaust, return `-1` instead.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["RLEIterator", "next", "next", "next", "next"]
[[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
Output:
[null, 8, 8, 5, -1]

Explanation:
RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // This maps to the sequence [8,8,8,5,5].
rLEIterator.next(2); // exhausts 2 terms of 8, returns 8. 1 term of 8 is remaining.
rLEIterator.next(1); // exhausts 1 term of 8, returns 8. 0 terms of 8 are remaining.
rLEIterator.next(1); // exhausts 1 term of 5, returns 5. 1 term of 5 is remaining.
rLEIterator.next(2); // exhausts 2 terms, that is 1 term of 5 and 1 term beyond the end. Returns -1.

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `next(n)`: O(number of compressed runs consumed)
Space Complexity: O(1) auxiliary space modifying or cursor-tracking the encoding array.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain cursor pointer `self.idx` pointing to the current count index in `encoding`.
When `next(n)` is called:
- While `self.idx < len(encoding)`:
  - If `encoding[self.idx] >= n`: decrement count `encoding[self.idx] -= n` and return `encoding[self.idx + 1]`.
  - Else: `n -= encoding[self.idx]`, `self.idx += 2`.
- If exhausted: return `-1`.
"""

import unittest
class RLEIterator:
    """Run-Length Encoded lazy sequence iterator."""

    def __init__(self, encoding: list[int]) -> None:
        self.encoding: list[int] = encoding
        self.idx: int = 0

    def next(self, n: int) -> int:
        while self.idx < len(self.encoding):
            if self.encoding[self.idx] >= n:
                self.encoding[self.idx] -= n
                return self.encoding[self.idx + 1]
            else:
                n -= self.encoding[self.idx]
                self.idx += 2
        return -1
class TestRLEIterator(unittest.TestCase):
    def test_example_1(self) -> None:
        rle = RLEIterator([3, 8, 0, 9, 2, 5])
        self.assertEqual(rle.next(2), 8)
        self.assertEqual(rle.next(1), 8)
        self.assertEqual(rle.next(1), 5)
        self.assertEqual(rle.next(2), -1)


if __name__ == "__main__":
    unittest.main()
