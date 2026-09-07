"""
LeetCode 1570: Dot Product of Two Sparse Vectors
Difficulty: Medium
Tags: Array, Hash Table, Two Pointers, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Given two sparse vectors, compute their dot product.

Implement class `SparseVector`:
- `SparseVector(int[] nums)` Initializes the object with the vector `nums`.
- `dotProduct(SparseVector vec)` Compute the dot product between the two sparse vectors.

A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `__init__`: O(N)
- `dotProduct`: O(min(K1, K2)) where K1, K2 are non-zero elements.
Space Complexity: O(K) to store non-zero entries.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store only non-zero entries in a hash map `non_zeros: dict[int, int]`.
When computing `dotProduct`:
Iterate over the smaller dictionary and multiply matching indices from the other vector.
"""

import unittest
class SparseVector:
    """Memory-efficient sparse vector representation using non-zero index map."""

    def __init__(self, nums: list[int]) -> None:
        self.non_zeros: dict[int, int] = {
            i: num for i, num in enumerate(nums) if num != 0
        }

    def dotProduct(self, vec: "SparseVector") -> int:
        total = 0
        # Iterate over smaller dictionary
        smaller, larger = (
            (self.non_zeros, vec.non_zeros)
            if len(self.non_zeros) < len(vec.non_zeros)
            else (vec.non_zeros, self.non_zeros)
        )
        for idx, val in smaller.items():
            if idx in larger:
                total += val * larger[idx]
        return total
class TestSparseVector(unittest.TestCase):
    def test_example_1(self) -> None:
        v1 = SparseVector([1, 0, 0, 2, 3])
        v2 = SparseVector([0, 3, 0, 4, 0])
        self.assertEqual(v1.dotProduct(v2), 8)


if __name__ == "__main__":
    unittest.main()
