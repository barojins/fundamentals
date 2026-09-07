"""
LeetCode 2353: Design a Food Rating System
Difficulty: Medium
Tags: Hash Table, Design, Heap (Priority Queue), Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a food rating system that can do the following:
- Modify the rating of a food item.
- Return the highest-rated food item for a type of cuisine. In case of a tie, return the food with the lexicographically smaller name.

Implement the `FoodRatings` class:
- `FoodRatings(String[] foods, String[] cuisines, int[] ratings)`
- `void changeRating(String food, int newRating)`
- `String highestRated(String cuisine)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output:
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `changeRating`: O(log N)
- `highestRated`: O(1) amortized
Space Complexity: O(N) for rating heaps per cuisine.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
For each cuisine, maintain a min-heap storing `(-rating, food_name)` tuples.
Also maintain:
- `food_to_cuisine: dict[str, str]`
- `food_to_rating: dict[str, int]`
When `highestRated(cuisine)` is called:
Lazy-clean the heap by discarding any entry whose `-rating != food_to_rating[food]`.
"""

import unittest
from collections import defaultdict
import heapq


class FoodRatings:
    """Food rating tracker by cuisine with lazy heap updates."""

    def __init__(
        self, foods: list[str], cuisines: list[str], ratings: list[int]
    ) -> None:
        self.food_cuisine: dict[str, str] = {}
        self.food_rating: dict[str, int] = {}
        self.cuisine_heaps: dict[str, list[tuple[int, str]]] = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_cuisine[food] = cuisine
            self.food_rating[food] = rating
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        cuisine = self.food_cuisine[food]
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        h = self.cuisine_heaps[cuisine]
        while h:
            neg_r, food = h[0]
            if -neg_r == self.food_rating[food]:
                return food
            heapq.heappop(h)
        return ""
class TestFoodRatings(unittest.TestCase):
    def test_example_1(self) -> None:
        fr = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7],
        )
        self.assertEqual(fr.highestRated("korean"), "kimchi")
        self.assertEqual(fr.highestRated("japanese"), "ramen")
        fr.changeRating("sushi", 16)
        self.assertEqual(fr.highestRated("japanese"), "sushi")
        fr.changeRating("ramen", 16)
        self.assertEqual(fr.highestRated("japanese"), "ramen")


if __name__ == "__main__":
    unittest.main()
