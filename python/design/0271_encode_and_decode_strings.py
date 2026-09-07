"""
LeetCode 271: Encode and Decode Strings
Difficulty: Medium
Tags: Array, String, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an algorithm to encode a list of strings to a single string and decode back.

Implement `Codec`:
- `String encode(List<String> strs)`
- `List<String> decode(String s)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: ["Hello","World"]
Output: ["Hello","World"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `encode`, `decode`: O(N)
Space Complexity: O(N)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use length-prefix framing: `f"{len(s)}#{s}"`.
"""

import unittest


class Codec:
    """Encodes a list of strings to a single string and decodes it back."""

    def encode(self, strs: list[str]) -> str:
        encoded_chunks = []
        for s in strs:
            encoded_chunks.append(f"{len(s)}#{s}")
        return "".join(encoded_chunks)

    def decode(self, s: str) -> list[str]:
        res: list[str] = []
        i = 0
        while i < len(s):
            delim_pos = s.find("#", i)
            length = int(s[i:delim_pos])
            start = delim_pos + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res


class TestCodec(unittest.TestCase):
    def test_standard_strings(self) -> None:
        codec = Codec()
        cases = [
            ["Hello", "World"],
            ["", ""],
            ["4#test", "###", "12#abc#def"],
            [],
        ]
        for case in cases:
            self.assertEqual(codec.decode(codec.encode(case)), case)


if __name__ == "__main__":
    unittest.main()
