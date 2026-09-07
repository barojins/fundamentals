"""
LeetCode 1797: Design Authentication Manager
Difficulty: Medium
Tags: Hash Table, Design, Doubly-Linked List

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
There is an authentication system that works with authentication tokens. For each session, the user will receive a new authentication token that will expire `timeToLive` seconds after the `currentTime`.

Implement the `AuthenticationManager` class:
- `AuthenticationManager(int timeToLive)` Constructs the `AuthenticationManager` and sets the `timeToLive`.
- `void generate(string tokenId, int currentTime)` Generates a new token with the given `tokenId` at the given `currentTime`.
- `void renew(string tokenId, int currentTime)` Renews the unexpired token with the given `tokenId` at the given `currentTime`. If the token does not exist or has expired, do nothing.
- `int countUnexpiredTokens(int currentTime)` Returns the number of unexpired tokens at the given `currentTime`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"]
[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
Output:
[null, null, null, 1, null, null, null, 0]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `generate`, `renew`: O(1)
- `countUnexpiredTokens`: O(N) where N is number of tokens.
Space Complexity: O(N) for tokens map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map `tokenId -> expiry_timestamp: dict[str, int]`.
- `generate(tokenId, currentTime)`: `tokens[tokenId] = currentTime + timeToLive`.
- `renew(tokenId, currentTime)`: if `tokenId in tokens` and `tokens[tokenId] > currentTime`, update `tokens[tokenId] = currentTime + timeToLive`.
- `countUnexpiredTokens(currentTime)`: count tokens with `expiry > currentTime`.
"""

import unittest
class AuthenticationManager:
    """Token authentication manager with TTL tracking."""

    def __init__(self, timeToLive: int) -> None:
        self.ttl: int = timeToLive
        self.tokens: dict[str, int] = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for exp in self.tokens.values() if exp > currentTime)
class TestAuthenticationManager(unittest.TestCase):
    def test_example_1(self) -> None:
        am = AuthenticationManager(5)
        am.renew("aaa", 1)
        am.generate("aaa", 2)
        self.assertEqual(am.countUnexpiredTokens(6), 1)
        am.generate("bbb", 7)
        am.renew("aaa", 8)
        am.renew("bbb", 10)
        self.assertEqual(am.countUnexpiredTokens(15), 0)


if __name__ == "__main__":
    unittest.main()
