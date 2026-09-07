"""
LeetCode 208: Implement Trie (Prefix Tree)
Difficulty: Medium
Tags: Hash Table, String, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.

Implement the `Trie` class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `insert`, `search`, `startsWith`: O(L) where L is string length.
Space Complexity: O(Total characters in trie * alphabet_size).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Each `TrieNode` has `children: dict[str, TrieNode]` and `is_end: bool`.
Traverse node by node for characters in word/prefix.
"""

import unittest


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    """Prefix Tree (Trie) for efficient string insertion, search, and prefix matching."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


class TestTrie(unittest.TestCase):
    def test_example_1(self) -> None:
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

    def test_overlapping_words(self) -> None:
        trie = Trie()
        words = ["car", "cart", "care", "cars", "cat"]
        for w in words:
            trie.insert(w)
        for w in words:
            self.assertTrue(trie.search(w))
        self.assertTrue(trie.startsWith("ca"))
        self.assertTrue(trie.startsWith("car"))
        self.assertFalse(trie.search("ca"))
        self.assertFalse(trie.search("dog"))


if __name__ == "__main__":
    unittest.main()
