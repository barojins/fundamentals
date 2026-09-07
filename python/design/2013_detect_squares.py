"""
LeetCode 2013: Detect Squares
Difficulty: Medium
Tags: Array, Hash Table, Design, Counting

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given a stream of points on the X-Y plane. You need to implement a data structure that, given a query point, counts the number of ways to choose three other points such that the four points form an axis-aligned square with positive area.

Implement the `DetectSquares` class:
- `DetectSquares()` Initializes the object with an empty data structure.
- `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
- `int count(int[] point)` Counts the number of ways to form axis-aligned squares with query point `[x, y]` as one of the four vertices.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output:
[null, null, null, null, 1, 0, null, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add`: O(1)
- `count`: O(number of unique stored points)
Space Complexity: O(P) for frequency map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store point frequencies: `points: Counter[(x, y)]`.
On `count([qx, qy])`:
Iterate over all stored diagonal candidate points `(px, py)`:
- Check if `|px - qx| == |py - qy| > 0` (forms a valid non-degenerate square diagonal).
- The other two required vertices are `(qx, py)` and `(px, qy)`.
- Add `points[(px, py)] * points[(qx, py)] * points[(px, qy)]` to total ways.
"""

import unittest
from collections import Counter


class DetectSquares:
    """Axis-aligned square counter from a 2D coordinate point stream."""

    def __init__(self) -> None:
        self.pts: Counter[tuple[int, int]] = Counter()

    def add(self, point: list[int]) -> None:
        self.pts[(point[0], point[1])] += 1

    def count(self, point: list[int]) -> int:
        qx, qy = point[0], point[1]
        total = 0

        for (px, py), count in self.pts.items():
            # Must form a valid square diagonal
            if abs(px - qx) == abs(py - qy) and px != qx:
                p2 = (qx, py)
                p3 = (px, qy)
                if p2 in self.pts and p3 in self.pts:
                    total += count * self.pts[p2] * self.pts[p3]

        return total
class TestDetectSquares(unittest.TestCase):
    def test_example_1(self) -> None:
        ds = DetectSquares()
        ds.add([3, 10])
        ds.add([11, 2])
        ds.add([3, 2])
        self.assertEqual(ds.count([11, 10]), 1)
        self.assertEqual(ds.count([14, 8]), 0)
        ds.add([11, 2])
        self.assertEqual(ds.count([11, 10]), 2)


if __name__ == "__main__":
    unittest.main()
