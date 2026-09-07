"""
LeetCode 1804: Implement Trie II (Prefix Tree)
Difficulty: Medium
Tags: Hash Table, String, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.

Implement the `Trie` class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `int countWordsEqualTo(String word)` Returns the number of instances of the string `word` in the trie.
- `int countWordsStartingWith(String prefix)` Returns the number of strings in the trie that have the string `prefix` as a prefix.
- `void erase(String word)` Erases the string `word` from the trie. It is guaranteed that `word` exists in the trie.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output:
[null, null, null, 2, 2, null, 1, 1, null, 0]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `insert`, `countWordsEqualTo`, `countWordsStartingWith`, `erase`: O(L) where L is length of word/prefix.
Space Complexity: O(Total characters across all words).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Each `TrieNode` stores:
- `pass_count: int` (how many words pass through this prefix node)
- `end_count: int` (how many words end exactly at this node)
- `children: dict[str, TrieNode]`
On `insert`: increment `pass_count` at each node, and `end_count` at the leaf.
On `erase`: decrement `pass_count` at each node, and `end_count` at the leaf.
"""

import unittest
class TrieNodeII:
    def __init__(self) -> None:
        self.children: dict[str, TrieNodeII] = {}
        self.pass_count: int = 0
        self.end_count: int = 0


class Trie:
    """Trie II supporting exact and prefix frequency counts and deletion."""

    def __init__(self) -> None:
        self.root = TrieNodeII()

    def insert(self, word: str) -> None:
        curr = self.root
        curr.pass_count += 1
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNodeII()
            curr = curr.children[char]
            curr.pass_count += 1
        curr.end_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.end_count

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.pass_count

    def erase(self, word: str) -> None:
        curr = self.root
        curr.pass_count -= 1
        for char in word:
            curr = curr.children[char]
            curr.pass_count -= 1
        curr.end_count -= 1
class TestTrie(unittest.TestCase):
    def test_example_1(self) -> None:
        trie = Trie()
        trie.insert("apple")
        trie.insert("apple")
        self.assertEqual(trie.countWordsEqualTo("apple"), 2)
        self.assertEqual(trie.countWordsStartingWith("app"), 2)
        trie.erase("apple")
        self.assertEqual(trie.countWordsEqualTo("apple"), 1)
        self.assertEqual(trie.countWordsStartingWith("app"), 1)
        trie.erase("apple")
        self.assertEqual(trie.countWordsStartingWith("app"), 0)


if __name__ == "__main__":
    unittest.main()
