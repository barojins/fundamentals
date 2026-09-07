"""
LeetCode 588: Design In-Memory File System
Difficulty: Hard
Tags: Hash Table, String, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that simulates an in-memory file system.

Implement the `FileSystem` class:
- `FileSystem()` Initializes the object of the system.
- `List<String> ls(String path)`
  - If `path` is a file path, returns a list that only contains this file's name.
  - If `path` is a directory path, returns the list of file and directory names in this directory in lexicographical order.
- `void mkdir(String path)` Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
- `void addContentToFile(String filePath, String content)`
  - If `filePath` does not exist, creates that file containing given `content`.
  - If `filePath` already exists, appends the given `content` to original content.
- `String readContentFromFile(String filePath)` Returns the content in the file at `filePath`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
Output:
[null,[],null,null,["a"],"hello"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `ls`: O(depth + entries log entries)
- `mkdir`: O(depth)
- `addContentToFile`: O(depth + len(content))
- `readContentFromFile`: O(depth)
Space Complexity: O(Total paths + file contents length).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Trie-like directory tree:
Each `FSNode` has:
- `is_file: bool`
- `content: str`
- `children: dict[str, FSNode]`
Splitting path by `/` lets you navigate from root node down the tree.
"""

import unittest
class FSNode:
    def __init__(self) -> None:
        self.is_file: bool = False
        self.content: str = ""
        self.children: dict[str, FSNode] = {}


class FileSystem:
    """In-memory hierarchical file system."""

    def __init__(self) -> None:
        self.root = FSNode()

    def _traverse(self, path: str) -> tuple[FSNode, list[str]]:
        parts = [p for p in path.split("/") if p]
        curr = self.root
        for part in parts:
            if part not in curr.children:
                curr.children[part] = FSNode()
            curr = curr.children[part]
        return curr, parts

    def ls(self, path: str) -> list[str]:
        node, parts = self._traverse(path)
        if node.is_file:
            return [parts[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node, _ = self._traverse(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node, _ = self._traverse(filePath)
        return node.content
class TestFileSystem(unittest.TestCase):
    def test_example_1(self) -> None:
        fs = FileSystem()
        self.assertEqual(fs.ls("/"), [])
        fs.mkdir("/a/b/c")
        fs.addContentToFile("/a/b/c/d", "hello")
        self.assertEqual(fs.ls("/"), ["a"])
        self.assertEqual(fs.readContentFromFile("/a/b/c/d"), "hello")


if __name__ == "__main__":
    unittest.main()
