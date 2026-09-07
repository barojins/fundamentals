"""
LeetCode 1912: Design Movie Rental System
Difficulty: Hard
Tags: Array, Hash Table, Design, Heap (Priority Queue), Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You have a movie renting company consisting of `n` shops. You want to implement a renting system that supports searching for, renting, and dropping movies, and also reporting the cheapest rented movies.

Implement the `MovieRentingSystem` class:
- `MovieRentingSystem(int n, int[][] entries)` Initializes the object with `n` shops and `entries` where `entries[i] = [shop_i, movie_i, price_i]`.
- `List<Integer> search(int movie)` Returns the cheapest <= 5 shops that have an unrented copy of `movie`, sorted by price ascending, then shop ID ascending.
- `void rent(int shop, int movie)` Rents the movie from the shop.
- `void drop(int shop, int movie)` Drops off a previously rented movie at the shop.
- `List<List<Integer>> report()` Returns the cheapest <= 5 rented movies across all shops, sorted by price ascending, then shop ID ascending, then movie ID ascending.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 5], [1, 2, 5], [2, 2, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
Output:
[null, [0], null, null, [[0, 1], [1, 2]], null, [0, 1, 2]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `search`: O(5 log K)
- `rent`, `drop`: O(log K)
- `report`: O(5 log R)
Space Complexity: O(Total entries) for ordered sets / sorted lists.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `price_map: dict[(shop, movie), price]`
- `unrented[movie]`: sorted list / heap of `(price, shop)`
- `rented`: sorted list / heap of `(price, shop, movie)`
Use binary search / `bisect` or SortedList to add and remove items in O(log N) time.
"""

import unittest
from collections import defaultdict
import bisect


class MovieRentingSystem:
    """Movie rental search, inventory management, and reporting system."""

    def __init__(self, n: int, entries: list[list[int]]) -> None:
        self.prices: dict[tuple[int, int], int] = {}
        # movie -> sorted list of (price, shop)
        self.unrented: dict[int, list[tuple[int, int]]] = defaultdict(list)
        # sorted list of (price, shop, movie)
        self.rented: list[tuple[int, int, int]] = []

        for shop, movie, price in entries:
            self.prices[(shop, movie)] = price
            self.unrented[movie].append((price, shop))

        for movie in self.unrented:
            self.unrented[movie].sort()

    def search(self, movie: int) -> list[int]:
        candidates = self.unrented.get(movie, [])
        return [shop for _, shop in candidates[:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        # Remove from unrented
        idx = bisect.bisect_left(self.unrented[movie], (price, shop))
        self.unrented[movie].pop(idx)
        # Add to rented
        bisect.insort(self.rented, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[(shop, movie)]
        # Remove from rented
        idx = bisect.bisect_left(self.rented, (price, shop, movie))
        self.rented.pop(idx)
        # Add to unrented
        bisect.insort(self.unrented[movie], (price, shop))

    def report(self) -> list[list[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]
class TestMovieRentingSystem(unittest.TestCase):
    def test_example_1(self) -> None:
        system = MovieRentingSystem(
        3, [[0, 1, 5], [0, 2, 5], [1, 2, 5], [2, 2, 5]]
        )
        self.assertEqual(system.search(1), [0])
        system.rent(0, 1)
        system.rent(1, 2)
        self.assertEqual(system.report(), [[0, 1], [1, 2]])
        system.drop(1, 2)
        self.assertEqual(system.search(2), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
