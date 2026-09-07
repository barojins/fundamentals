"""
LeetCode 3391: Design a 3D Binary Matrix with Efficient Layer Tracking
Difficulty: Medium
Tags: Array, Hash Table, Design, Matrix

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a 3D Binary Matrix of size `n x n x n` initialized to all 0s, with layer tracking along the z-axis (matrices `0` to `n - 1`).

Implement the `Matrix3D` class:
- `Matrix3D(int n)` Initializes an `n x n x n` 3D binary matrix with all 0s.
- `void setCell(int x, int y, int z)` Sets `matrix[x][y][z] = 1`.
- `void unsetCell(int x, int y, int z)` Sets `matrix[x][y][z] = 0`.
- `int largestMatrix()` Returns the index of the 2D layer (z) with the largest count of 1s. If tied, return the largest z index.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Matrix3D", "setCell", "setCell", "largestMatrix", "unsetCell", "largestMatrix"]
[[3], [0, 0, 1], [0, 1, 1], [], [0, 1, 1], []]
Output:
[null, null, null, 1, null, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `setCell`, `unsetCell`: O(1)
- `largestMatrix`: O(N) layer scan
Space Complexity: O(N^3) or sparse set of active cells.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Track 1s count per layer `layer_ones: list[int] = [0] * n`.
Maintain active 1s in a set `active_cells: set[(x, y, z)]`.
When `largestMatrix()` is called:
Find max count and break ties with largest layer index.
"""

import unittest
class Matrix3D:
    """3D binary matrix with layer population tracking."""

    def __init__(self, n: int) -> None:
        self.n: int = n
        self.layer_counts: list[int] = [0] * n
        self.active: set[tuple[int, int, int]] = set()

    def setCell(self, x: int, y: int, z: int) -> None:
        if (x, y, z) not in self.active:
            self.active.add((x, y, z))
            self.layer_counts[z] += 1

    def unsetCell(self, x: int, y: int, z: int) -> None:
        if (x, y, z) in self.active:
            self.active.remove((x, y, z))
            self.layer_counts[z] -= 1

    def largestMatrix(self) -> int:
        best_z = self.n - 1
        max_c = self.layer_counts[best_z]
        for z in range(self.n - 1, -1, -1):
            if self.layer_counts[z] > max_c:
                max_c = self.layer_counts[z]
                best_z = z
        return best_z

class TestMatrix3D(unittest.TestCase):
    def test_example_1(self) -> None:
        m3d = Matrix3D(3)
        m3d.setCell(0, 0, 1)
        m3d.setCell(0, 1, 1)
        self.assertEqual(m3d.largestMatrix(), 1)
        m3d.unsetCell(0, 1, 1)
        self.assertEqual(m3d.largestMatrix(), 1)
        m3d.unsetCell(0, 0, 1)
        self.assertEqual(m3d.largestMatrix(), 2)


if __name__ == "__main__":
    unittest.main()
