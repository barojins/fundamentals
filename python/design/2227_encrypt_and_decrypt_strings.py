"""
LeetCode 2227: Encrypt and Decrypt Strings
Difficulty: Hard
Tags: Array, Hash Table, String, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given a character array `keys` containing unique characters and a string array `values` containing strings of length 2. You are also given another string array `dictionary` that contains all allowed strings that can be decrypted.

Implement the `Encrypter` class:
- `Encrypter(char[] keys, String[] values, String[] dictionary)`
- `String encrypt(String word1)` Encrypts `word1` by replacing each character with its mapped value. If any char is not in `keys`, return `""`.
- `int decrypt(String word2)` Returns the number of possible strings in `dictionary` that encrypt to `word2`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Encrypter", "encrypt", "decrypt"]
[[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]
Output:
[null, "eizfeiam", 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N * L) where dictionary words are pre-encrypted into a frequency map.
- `encrypt`: O(L)
- `decrypt`: O(1) hash map lookup!
Space Complexity: O(N * L) for encrypted dictionary frequencies.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Precompute `self.encrypted_dict_counts: Counter[str]` during `__init__`!
For each word in `dictionary`, call `encrypt(word)`. If valid, increment its count in `self.encrypted_dict_counts`.
Then `decrypt(word2)` is just `self.encrypted_dict_counts[word2]` in O(1)!
"""

import unittest
from collections import Counter


class Encrypter:
    """String encrypter with O(1) decryption via pre-encrypted dictionary counts."""

    def __init__(
        self, keys: list[str], values: list[str], dictionary: list[str]
    ) -> None:
        self.key_to_val: dict[str, str] = dict(zip(keys, values))
        self.encrypted_counts: Counter[str] = Counter()

        for word in dictionary:
            enc = self.encrypt(word)
            if enc:
                self.encrypted_counts[enc] += 1

    def encrypt(self, word1: str) -> str:
        res = []
        for char in word1:
            if char not in self.key_to_val:
                return ""
            res.append(self.key_to_val[char])
        return "".join(res)

    def decrypt(self, word2: str) -> int:
        return self.encrypted_counts[word2]
class TestEncrypter(unittest.TestCase):
    def test_example_1(self) -> None:
        encrypter = Encrypter(
        ["a", "b", "c", "d"],
        ["ei", "zf", "ei", "am"],
        [
        "abcd",
        "acbd",
        "adbc",
        "badc",
        "dacb",
        "cadb",
        "cbda",
        "abad",
        ],
        )
        self.assertEqual(encrypter.encrypt("abcd"), "eizfeiam")
        self.assertEqual(encrypter.decrypt("eizfeiam"), 2)


if __name__ == "__main__":
    unittest.main()
