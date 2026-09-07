"""
LeetCode 3815: Design Auction System
Difficulty: Medium
Tags: Hash Table, Design, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an auction management system for managing item biddings.

Implement the `AuctionSystem` class:
- `AuctionSystem()`
- `void createAuction(int auctionId, String itemId, int reservePrice)`
- `bool placeBid(int auctionId, int bidderId, int bidAmount)` Returns `true` if bid accepted (strictly higher than current highest and >= reserve).
- `int closeAuction(int auctionId)` Returns winning `bidderId` or `-1` if no valid bid placed.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["AuctionSystem", "createAuction", "placeBid", "placeBid", "closeAuction"]
[[], [1, "painting", 100], [1, 10, 150], [1, 20, 140], [1]]
Output:
[null, null, true, false, 10]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `createAuction`, `placeBid`, `closeAuction`: O(1)
Space Complexity: O(Auctions).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store per-auction state:
`{ "reserve": int, "highest_bid": int, "winner": int, "is_open": bool }`.
"""

import unittest
class AuctionSystem:
    """Real-time item auction management system."""

    def __init__(self) -> None:
        self.auctions: dict[int, dict] = {}

    def createAuction(
        self, auctionId: int, itemId: str, reservePrice: int
    ) -> None:
        self.auctions[auctionId] = {
            "itemId": itemId,
            "reserve": reservePrice,
            "highest_bid": reservePrice - 1,
            "winner": -1,
            "open": True,
        }

    def placeBid(self, auctionId: int, bidderId: int, bidAmount: int) -> bool:
        if auctionId not in self.auctions or not self.auctions[auctionId]["open"]:
            return False

        auc = self.auctions[auctionId]
        if bidAmount >= auc["reserve"] and bidAmount > auc["highest_bid"]:
            auc["highest_bid"] = bidAmount
            auc["winner"] = bidderId
            return True

        return False

    def closeAuction(self, auctionId: int) -> int:
        if auctionId not in self.auctions or not self.auctions[auctionId]["open"]:
            return -1
        self.auctions[auctionId]["open"] = False
        return self.auctions[auctionId]["winner"]
class TestAuctionSystem(unittest.TestCase):
    def test_example_1(self) -> None:
        aus = AuctionSystem()
        aus.createAuction(1, "painting", 100)
        self.assertTrue(aus.placeBid(1, 10, 150))
        self.assertFalse(aus.placeBid(1, 20, 140))
        self.assertEqual(aus.closeAuction(1), 10)


if __name__ == "__main__":
    unittest.main()
