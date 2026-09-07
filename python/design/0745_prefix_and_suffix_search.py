"""
LeetCode 745: Prefix and Suffix Search
Difficulty: Hard
Tags: Hash Table, String, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the `WordFilter` class:
- `WordFilter(string[] words)` Initializes the object with the `words` in the dictionary.
- `f(string pref, string suff)` Returns the index of the word in the dictionary, which has the prefix `pref` and the suffix `suff`. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return `-1`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output:
[null, 0]

Explanation:
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N * L^2) where N is number of words and L is max length.
- `f(pref, suff)`: O(P + S) prefix/suffix search in combined trie or hash map.
Space Complexity: O(N * L^2) to index all suffix#prefix combinations.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
For each word at index `i`, insert all combinations `suffix + '#' + word` into a Trie or hash map.
For example, for word `"apple"`, insert:
`apple#apple`, `pple#apple`, `ple#apple`, `le#apple`, `e#apple`, `#apple`.
To query `f(pref, suff)`: search key `suff + '#' + pref` directly!
"""

import unittest
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.weight: int = -1


class WordFilter:
    """Prefix and Suffix Search using suffix#prefix combined Trie."""

    def __init__(self, words: list[str]) -> None:
        self.root = TrieNode()
        for weight, word in enumerate(words):
            word_len = len(word)
            for i in range(word_len + 1):
                suffix = word[i:]
                wrapped = suffix + "{" + word  # '{' comes right after 'z'
                curr = self.root
                curr.weight = weight
                for char in wrapped:
                    if char not in curr.children:
                        curr.children[char] = TrieNode()
                    curr = curr.children[char]
                    curr.weight = weight

    def f(self, pref: str, suff: str) -> int:
        target = suff + "{" + pref
        curr = self.root
        for char in target:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        return curr.weight
class TestWordFilter(unittest.TestCase):
    def test_example_1(self) -> None:
        wf = WordFilter(["apple"])
        self.assertEqual(wf.f("a", "e"), 0)
        self.assertEqual(wf.f("b", ""), -1)


if __name__ == "__main__":
    unittest.main()
