"""
LeetCode 676: Implement Magic Dictionary
Difficulty: Medium
Tags: Hash Table, String, Depth-First Search, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure that is initialized with a list of different words. Provided a new word, you should determine if you can change exactly one character in this word to match any word in the data structure.

Implement the `MagicDictionary` class:
- `MagicDictionary()` Initializes the object.
- `void buildDict(String[] dictionary)` Sets the data structure with an array of distinct strings `dictionary`.
- `bool search(String searchWord)` Returns `true` if you can change exactly one character in `searchWord` to match any string in the dictionary, and `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output:
[null, null, false, true, false, false]

Explanation:
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False (requires changing exactly 1 char)
magicDictionary.search("hhllo"); // return True ('h' -> 'e' matches "hello")
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `buildDict`: O(N * L)
- `search`: O(L * 26) or O(L * words_of_same_length)
Space Complexity: O(N * L) to store words grouped by length.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Group words by their string length: `self.words_by_len: dict[int, list[str]]`.
For `search(searchWord)`:
Iterate over candidate words of same length `len(searchWord)`.
Count differing character positions. If differences == 1, return `True`.
"""

import unittest
from collections import defaultdict


class MagicDictionary:
    """Dictionary supporting search with exactly one character difference."""

    def __init__(self) -> None:
        self.words_by_len: dict[int, list[str]] = defaultdict(list)

    def buildDict(self, dictionary: list[str]) -> None:
        self.words_by_len.clear()
        for word in dictionary:
            self.words_by_len[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        candidates = self.words_by_len[len(searchWord)]
        for cand in candidates:
            diff_count = 0
            for c1, c2 in zip(searchWord, cand):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 1:
                        break
            if diff_count == 1:
                return True
        return False
class TestMagicDictionary(unittest.TestCase):
    def test_example_1(self) -> None:
        md = MagicDictionary()
        md.buildDict(["hello", "leetcode"])
        self.assertFalse(md.search("hello"))
        self.assertTrue(md.search("hhllo"))
        self.assertFalse(md.search("hell"))
        self.assertFalse(md.search("leetcoded"))


if __name__ == "__main__":
    unittest.main()
