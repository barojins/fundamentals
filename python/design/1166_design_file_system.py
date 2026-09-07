"""
LeetCode 1166: Design File System
Difficulty: Medium
Tags: Hash Table, String, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: `/` followed by one or more lowercase English letters. For example, `"/leetcode"` and `"/leetcode/problems"` are valid paths while an empty string `""` and `"/"` are not.

Implement the `FileSystem` class:
- `bool createPath(string path, int value)` Creates a new `path` and associates a `value` to it if possible and returns `true`. Returns `false` if the path already exists or its parent path doesn't exist.
- `int get(string path)` Returns the value associated with `path` or returns `-1` if the path doesn't exist.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output:
[null,true,1]

Example 2:
Input:
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output:
[null,true,true,2,false,-1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `createPath`: O(L) where L is path string length.
- `get`: O(L)
Space Complexity: O(Total paths created).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a hash map `paths: dict[str, int]` (or Trie).
To create `/a/b/c`:
1. Check that `path not in paths`.
2. Extract parent path: `parent = path[:path.rfind('/')]`.
3. Check `parent == ""` (root) or `parent in paths`.
4. Store `paths[path] = value`.
"""

import unittest
class FileSystem:
    """Path-value store enforcing parent directory existence on creation."""

    def __init__(self) -> None:
        self.paths: dict[str, int] = {"": 0}

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/" or path in self.paths:
            return False

        parent = path[: path.rfind("/")]
        if parent not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)
class TestFileSystem(unittest.TestCase):
    def test_example_1(self) -> None:
        fs = FileSystem()
        self.assertTrue(fs.createPath("/a", 1))
        self.assertEqual(fs.get("/a"), 1)
        self.assertTrue(fs.createPath("/leet", 1))
        self.assertTrue(fs.createPath("/leet/code", 2))
        self.assertEqual(fs.get("/leet/code"), 2)
        self.assertFalse(fs.createPath("/c/d", 1))
        self.assertEqual(fs.get("/c"), -1)


if __name__ == "__main__":
    unittest.main()
