"""
LeetCode 535: Encode and Decode TinyURL
Difficulty: Medium
Tags: Hash Table, String, Design, Hash Function

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the `Codec` class:
- `Codec()` Initializes the object of the system.
- `String encode(String longUrl)` Returns a tiny URL for the given `longUrl`.
- `String decode(String shortUrl)` Returns the original long URL for the given `shortUrl`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"
Explanation:
Codec codec = new Codec();
codec.decode(codec.encode(url)); // returns the original url

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `encode`: O(1) average.
- `decode`: O(1)
Space Complexity: O(N) where N is number of shortened URLs.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Generate a random 6-character alphanumeric key (or auto-incrementing Base62 ID).
Maintain:
- `code_to_url: dict[str, str]`
- `url_to_code: dict[str, str]` (for deduplication)
"""

import unittest
import random
import string


class Codec:
    """URL Shortener (TinyURL) using random 6-character Base62 alphanumeric tokens."""

    def __init__(self) -> None:
        self.alphabet: str = string.ascii_letters + string.digits
        self.code_to_url: dict[str, str] = {}
        self.url_to_code: dict[str, str] = {}
        self.base_url: str = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]

        while True:
            code = "".join(random.choices(self.alphabet, k=6))
            if code not in self.code_to_url:
                break

        self.code_to_url[code] = longUrl
        self.url_to_code[longUrl] = code
        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url[code]
class TestCodec(unittest.TestCase):
    def test_example_1(self) -> None:
        codec = Codec()
        url = "https://leetcode.com/problems/design-tinyurl"
        short_url = codec.encode(url)
        self.assertEqual(codec.decode(short_url), url)


if __name__ == "__main__":
    unittest.main()
