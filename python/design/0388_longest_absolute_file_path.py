"""
LeetCode 388: Longest Absolute File Path
Difficulty: Medium
Tags: String, Stack, Depth-First Search

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Suppose we have a file system represented as a string `input` where `
` indicates a new line and `	` indicates a sub-directory or file level.

Find the length of the longest absolute path to a file within our file system. If there is no file in the system, return `0`.

Note: A file must contain a `.` extension.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: input = "dir
	subdir1
	subdir2
		file.ext"
Output: 20
Explanation: We have only one file, and its path is "dir/subdir2/file.ext" of length 20.

Example 2:
Input: input = "dir
	subdir1
		file1.ext
		subsubdir1
	subdir2
		subsubdir2
			file2.ext"
Output: 32

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity: O(N) where N is length of the string.
Space Complexity: O(D) where D is the maximum directory depth.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a hash map or stack `path_len: dict[int, int]` mapping depth -> cumulative path length up to that depth.
For each line:
- Count leading `	`s to get `depth`.
- Length of current name is `len(name)`.
- If it's a directory: `path_len[depth] = path_len.get(depth - 1, 0) + len(name) + 1` (accounting for `/`).
- If it's a file: `max_len = max(max_len, path_len.get(depth - 1, 0) + len(name))`.
"""

import unittest


class Solution:
    """Parses tab-delimited file hierarchy to find the longest file path."""

    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len: dict[int, int] = {-1: 0}

        for line in input.split("\n"):
            depth = line.count("\t")
            name = line.lstrip("\t")

            if "." in name:
                total_len = path_len[depth - 1] + len(name)
                max_len = max(max_len, total_len)
            else:
                path_len[depth] = path_len[depth - 1] + len(name) + 1  # +1 for '/'

        return max_len


class TestSolution(unittest.TestCase):
    def test_example_1(self) -> None:
        s = Solution()
        self.assertEqual(
            s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"), 20
        )

    def test_example_2(self) -> None:
        s = Solution()
        inp = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        self.assertEqual(s.lengthLongestPath(inp), 32)

    def test_no_file(self) -> None:
        s = Solution()
        self.assertEqual(s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2"), 0)


if __name__ == "__main__":
    unittest.main()
