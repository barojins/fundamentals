"""
LeetCode 2424: Longest Uploaded Prefix
Difficulty: Medium
Tags: Binary Search, Union Find, Design, Binary Indexed Tree, Segment Tree, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given a stream of `n` videos, each represented by a distinct number from `1` to `n` that you need to upload one by one.

Implement the `LUPrefix` class:
- `LUPrefix(int n)` Initializes the object for a stream of `n` videos.
- `void upload(int video)` Uploads the given `video`.
- `int longest()` Returns the length of the longest prefix of uploaded videos.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["LUPrefix", "upload", "longest", "upload", "upload", "longest"]
[[4], [3], [], [1], [2], []]
Output:
[null, null, 0, null, null, 3]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `upload`: O(1) amortized
- `longest`: O(1)
Space Complexity: O(N) for uploaded boolean flags.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain boolean array `uploaded = [False] * (n + 2)` and pointer `ptr = 0`.
On `upload(video)`:
- `uploaded[video] = True`
- While `uploaded[ptr + 1]`: `ptr += 1`.
`longest()` returns `ptr` in O(1)!
"""

import unittest
class LUPrefix:
    """Tracks continuous prefix of uploaded videos with O(1) amortized progress."""

    def __init__(self, n: int) -> None:
        self.uploaded: list[bool] = [False] * (n + 2)
        self.longest_prefix: int = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.uploaded[self.longest_prefix + 1]:
            self.longest_prefix += 1

    def longest(self) -> int:
        return self.longest_prefix
class TestLUPrefix(unittest.TestCase):
    def test_example_1(self) -> None:
        server = LUPrefix(4)
        server.upload(3)
        self.assertEqual(server.longest(), 0)
        server.upload(1)
        server.upload(2)
        self.assertEqual(server.longest(), 3)


if __name__ == "__main__":
    unittest.main()
