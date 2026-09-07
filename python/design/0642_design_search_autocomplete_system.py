"""
LeetCode 642: Design Search Autocomplete System
Difficulty: Hard
Tags: String, Depth-First Search, Design, Trie, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character `'#'`).

For each character they type except `'#'`, you need to return the top 3 historical hot sentences that have the same prefix as the part of sentence already typed. Here are the specific rules:
- The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
- The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
- If less than 3 hot sentences exist, return as many as you can.
- When the input is `'#'`, it means the sentence ends, and you should record this sentence as a historical sentence in the system.

Implement the `AutocompleteSystem` class:
- `AutocompleteSystem(String[] sentences, int[] times)` Initializes the object with the `sentences` and `times` arrays.
- `List<String> input(char c)` Returns the top 3 hot sentences, or empty list if `'#'` terminates input.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output:
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N * L) where N is number of sentences and L is length.
- `input(c)`: O(P + S log S) where P is prefix length and S is candidate sentence matches.
Space Complexity: O(Total characters in trie + sentence frequency map).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Trie where each node stores a hash map `counts: dict[str, int]` of all sentences that pass through this node.
- During typing: traverse down to `curr_node.children[c]`. The top 3 sentences are obtained by sorting `curr_node.counts.items()` with key `(-count, sentence)`.
- When `'#'` is entered: insert or increment the typed buffer sentence into the Trie from root, then reset current buffer and pointer to root.
"""

import unittest
from collections import defaultdict


class TrieAutocompleteNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieAutocompleteNode] = {}
        self.counts: dict[str, int] = defaultdict(int)


class AutocompleteSystem:
    """Search autocomplete system returning top-3 hottest sentences matching typed prefix."""

    def __init__(self, sentences: list[str], times: list[int]) -> None:
        self.root = TrieAutocompleteNode()
        self.curr_node: TrieAutocompleteNode | None = self.root
        self.curr_buffer: list[str] = []

        for s, t in zip(sentences, times):
            self._add_sentence(s, t)

    def _add_sentence(self, sentence: str, count: int) -> None:
        curr = self.root
        for char in sentence:
            if char not in curr.children:
                curr.children[char] = TrieAutocompleteNode()
            curr = curr.children[char]
            curr.counts[sentence] += count

    def input(self, c: str) -> list[str]:
        if c == "#":
            sentence = "".join(self.curr_buffer)
            self._add_sentence(sentence, 1)
            self.curr_buffer = []
            self.curr_node = self.root
            return []

        self.curr_buffer.append(c)
        if self.curr_node and c in self.curr_node.children:
            self.curr_node = self.curr_node.children[c]
            # Sort candidate sentences by (-count, sentence)
            candidates = sorted(
                self.curr_node.counts.items(), key=lambda item: (-item[1], item[0])
            )
            return [s for s, _ in candidates[:3]]
        else:
            self.curr_node = None
            return []
class TestAutocompleteSystem(unittest.TestCase):
    def test_example_1(self) -> None:
        system = AutocompleteSystem(
        ["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]
        )
        self.assertEqual(system.input("i"), ["i love you", "island", "i love leetcode"])
        self.assertEqual(system.input(" "), ["i love you", "i love leetcode"])
        self.assertEqual(system.input("a"), [])
        self.assertEqual(system.input("#"), [])


if __name__ == "__main__":
    unittest.main()
