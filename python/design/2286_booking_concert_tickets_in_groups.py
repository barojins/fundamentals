"""
LeetCode 2286: Booking Concert Tickets in Groups
Difficulty: Hard
Tags: Binary Search, Design, Binary Indexed Tree, Segment Tree

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A concert hall has `n` rows numbered from `0` to `n - 1`, each with `m` seats, numbered from `0` to `m - 1`. You need to design a ticketing system that can allocate seats in two ways:
1. `gather(k, maxRow)`: Allocate `k` contiguous seats in the same row from row `0` to `maxRow`. Returns `[row, first_seat_index]` or `[]` if not possible.
2. `scatter(k, maxRow)`: Allocate `k` seats across one or more rows from row `0` to `maxRow`. Returns `true` if successful, `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["BookMyShow", "gather", "gather", "scatter", "scatter"]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
Output:
[null, [0, 0], [], true, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `gather`: O(log N) using Segment Tree (tracking max available seats per row).
- `scatter`: O(log N + rows_filled) using Segment Tree (tracking sum of available seats).
Space Complexity: O(N) for Segment Tree.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Segment Tree where each node maintains:
- `max_free`: maximum free seats in any single row within the subtree range.
- `sum_free`: total free seats across all rows within the subtree range.
- `gather(k, maxRow)`: binary search down segment tree for lowest row index <= maxRow with `max_free >= k`.
- `scatter(k, maxRow)`: verify `query_sum(0, maxRow) >= k`, then allocate from lowest available row forward.
"""

import unittest
class BookMyShow:
    """Segment-tree concert hall seating manager."""

    def __init__(self, n: int, m: int) -> None:
        self.n: int = n
        self.m: int = m
        self.tree_max: list[int] = [0] * (4 * n)
        self.tree_sum: list[int] = [0] * (4 * n)
        self.occupied: list[int] = [0] * n  # occupied seats per row
        self.first_available_row: int = 0
        self._build(1, 0, n - 1)

    def _build(self, node: int, l: int, r: int) -> None:
        if l == r:
            self.tree_max[node] = self.m
            self.tree_sum[node] = self.m
            return
        mid = (l + r) // 2
        self._build(2 * node, l, mid)
        self._build(2 * node + 1, mid + 1, r)
        self.tree_max[node] = max(
            self.tree_max[2 * node], self.tree_max[2 * node + 1]
        )
        self.tree_sum[node] = self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]

    def _update(self, node: int, l: int, r: int, row: int, free: int) -> None:
        if l == r:
            self.tree_max[node] = free
            self.tree_sum[node] = free
            return
        mid = (l + r) // 2
        if row <= mid:
            self._update(2 * node, l, mid, row, free)
        else:
            self._update(2 * node + 1, mid + 1, r, row, free)
        self.tree_max[node] = max(
            self.tree_max[2 * node], self.tree_max[2 * node + 1]
        )
        self.tree_sum[node] = self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]

    def _query_sum(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.tree_sum[node]
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res += self._query_sum(2 * node, l, mid, ql, qr)
        if qr > mid:
            res += self._query_sum(2 * node + 1, mid + 1, r, ql, qr)
        return res

    def _find_row_for_gather(
        self, node: int, l: int, r: int, maxRow: int, k: int
    ) -> int:
        if self.tree_max[node] < k or l > maxRow:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        res = self._find_row_for_gather(2 * node, l, mid, maxRow, k)
        if res != -1:
            return res
        return self._find_row_for_gather(2 * node + 1, mid + 1, r, maxRow, k)

    def gather(self, k: int, maxRow: int) -> list[int]:
        row = self._find_row_for_gather(1, 0, self.n - 1, maxRow, k)
        if row == -1:
            return []
        start_seat = self.occupied[row]
        self.occupied[row] += k
        free = self.m - self.occupied[row]
        self._update(1, 0, self.n - 1, row, free)
        return [row, start_seat]

    def scatter(self, k: int, maxRow: int) -> bool:
        total_available = self._query_sum(1, 0, self.n - 1, 0, maxRow)
        if total_available < k:
            return False

        rem = k
        row = self.first_available_row
        while rem > 0 and row <= maxRow:
            free = self.m - self.occupied[row]
            if free > 0:
                take = min(free, rem)
                self.occupied[row] += take
                rem -= take
                self._update(1, 0, self.n - 1, row, self.m - self.occupied[row])
            if self.occupied[row] == self.m:
                row += 1
        self.first_available_row = row
        return True
class TestBookMyShow(unittest.TestCase):
    def test_example_1(self) -> None:
        bms = BookMyShow(2, 5)
        self.assertEqual(bms.gather(4, 0), [0, 0])
        self.assertEqual(bms.gather(2, 0), [])
        self.assertTrue(bms.scatter(5, 1))
        self.assertFalse(bms.scatter(5, 1))


if __name__ == "__main__":
    unittest.main()
