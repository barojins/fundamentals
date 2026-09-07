"""
LeetCode 1656: Design an Ordered Stream
Difficulty: Easy
Tags: Array, Hash Table, Design, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
There is a stream of `n` `(idKey, value)` pairs arriving in an arbitrary order, where `idKey` is an integer between `1` and `n` and `value` is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk of values after each insertion.

Implement the `OrderedStream` class:
- `OrderedStream(int n)` Initializes the stream to take `n` values.
- `String[] insert(int idKey, String value)` Inserts the pair into the stream and returns the largest possible contiguous chunk of values starting from the smallest missing ID.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output:
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `insert`: O(N) total across all insertions.
Space Complexity: O(N) for array storage.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store stream elements in 1-indexed array `stream = [None] * (n + 1)` and maintain pointer `ptr = 1`.
On `insert(idKey, value)`:
- `stream[idKey] = value`
- While `ptr < len(stream)` and `stream[ptr] is not None`: collect `stream[ptr]` and increment `ptr`.
- Return collected chunk.
"""

import unittest
class OrderedStream:
    """Consecutive ordered stream buffer."""

    def __init__(self, n: int) -> None:
        self.stream: list[str | None] = [None] * (n + 1)
        self.ptr: int = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value
        chunk: list[str] = []

        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            chunk.append(self.stream[self.ptr])  # type: ignore
            self.ptr += 1

        return chunk
class TestOrderedStream(unittest.TestCase):
    def test_example_1(self) -> None:
        os = OrderedStream(5)
        self.assertEqual(os.insert(3, "ccccc"), [])
        self.assertEqual(os.insert(1, "aaaaa"), ["aaaaa"])
        self.assertEqual(os.insert(2, "bbbbb"), ["bbbbb", "ccccc"])
        self.assertEqual(os.insert(5, "eeeee"), [])
        self.assertEqual(os.insert(4, "ddddd"), ["ddddd", "eeeee"])


if __name__ == "__main__":
    unittest.main()
