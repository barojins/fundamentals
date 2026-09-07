"""
LeetCode 211: Design Add and Search Words Data Structure
Difficulty: Medium
Tags: String, Depth-First Search, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that supports adding new words and finding if a string matches any previously added string with wildcard `.` support.

Implement the `WordDictionary` class:
- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure.
- `bool search(word)` Returns `true` if there is any string matching `word`. `word` may contain dots `.` matching any letter.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output:
[null,null,null,null,false,true,true,true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addWord`: O(L)
- `search`: O(L) without wildcards; O(26^L) worst case with dots.
Space Complexity: O(Total characters).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Trie with DFS backtracking on `.`. If `.`, branch through all `node.children.values()`.
"""

import unittest


class WordDictionaryNode:
    def __init__(self) -> None:
        self.children: dict[str, WordDictionaryNode] = {}
        self.is_end: bool = False


class WordDictionary:
    """Trie-based dictionary supporting exact word search and wildcard '.' search."""

    def __init__(self) -> None:
        self.root = WordDictionaryNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionaryNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: WordDictionaryNode, index: int) -> bool:
            if index == len(word):
                return node.is_end

            char = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)


class TestWordDictionary(unittest.TestCase):
    def test_example_1(self) -> None:
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        self.assertFalse(wd.search("pad"))
        self.assertTrue(wd.search("bad"))
        self.assertTrue(wd.search(".ad"))
        self.assertTrue(wd.search("b.."))

    def test_wildcards_everywhere(self) -> None:
        wd = WordDictionary()
        wd.addWord("a")
        wd.addWord("ab")
        self.assertTrue(wd.search("."))
        self.assertTrue(wd.search(".."))
        self.assertFalse(wd.search("..."))


if __name__ == "__main__":
    unittest.main()
