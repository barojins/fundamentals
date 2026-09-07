"""
LeetCode 1032: Stream of Characters
Difficulty: Hard
Tags: Array, String, Design, Trie, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of words.

For example, if `words = ["abc", "xyz"]` and the stream of characters arrives as `'a'`, `'b'`, `'c'`, then the query for `'c'` should return `true` since the suffix `"abc"` matches the word `"abc"`.

Implement the `StreamChecker` class:
- `StreamChecker(String[] words)` Initializes the object with the given words.
- `boolean query(char letter)` Accepts a new character from the stream and returns `true` if any non-empty suffix from the stream matches a word in `words`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output:
[null, false, false, false, true, false, true, false, false, false, false, false, true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N * L) where N is number of words and L is max length.
- `query(letter)`: O(L) where L is maximum word length.
Space Complexity: O(N * L) for reversed word Trie.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Insert all words reversed into a Trie!
Maintain a stream history `stream: list[str]`.
When `query(letter)` is called:
- Append `letter` to stream history.
- Traverse the Trie backwards from `stream[-1]` down `stream[-2]`, etc.
- If at any step `node.is_end` is True, return `True`. If child not found, return `False`.
"""

import unittest
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class StreamChecker:
    """Stream suffix matching using a reverse-word Trie."""

    def __init__(self, words: list[str]) -> None:
        self.root = TrieNode()
        self.stream: list[str] = []
        self.max_len: int = 0

        for word in words:
            self.max_len = max(self.max_len, len(word))
            curr = self.root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_end = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        # We only need to keep at most max_len characters in history
        if len(self.stream) > self.max_len:
            self.stream.pop(0)

        curr = self.root
        for char in reversed(self.stream):
            if char not in curr.children:
                return False
            curr = curr.children[char]
            if curr.is_end:
                return True
        return False
class TestStreamChecker(unittest.TestCase):
    def test_example_1(self) -> None:
        sc = StreamChecker(["cd", "f", "kl"])
        self.assertFalse(sc.query("a"))
        self.assertFalse(sc.query("b"))
        self.assertFalse(sc.query("c"))
        self.assertTrue(sc.query("d"))
        self.assertFalse(sc.query("e"))
        self.assertTrue(sc.query("f"))
        self.assertFalse(sc.query("g"))
        self.assertFalse(sc.query("h"))
        self.assertFalse(sc.query("i"))
        self.assertFalse(sc.query("j"))
        self.assertFalse(sc.query("k"))
        self.assertTrue(sc.query("l"))


if __name__ == "__main__":
    unittest.main()
