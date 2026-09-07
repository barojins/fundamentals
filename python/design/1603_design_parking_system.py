"""
LeetCode 1603: Design Parking System
Difficulty: Easy
Tags: Design, Simulation, Counting

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the `ParkingSystem` class:
- `ParkingSystem(int big, int medium, int small)` Initializes object of the `ParkingSystem` class.
- `bool addCar(int carType)` Checks whether there is a parking space of `carType` for the car that wants to get into the parking lot. `carType` can be of three kinds: big (1), medium (2), or small (3). Returns `true` if parked, `false` otherwise.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output:
[null, true, true, false, false]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addCar`: O(1)
Space Complexity: O(1)

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store available counts in a map/array: `slots = [0, big, medium, small]`.
On `addCar(carType)`: if `slots[carType] > 0`: decrement and return `True`; else return `False`.
"""

import unittest
class ParkingSystem:
    """Fixed-capacity parking lot allocation system."""

    def __init__(self, big: int, medium: int, small: int) -> None:
        self.slots: list[int] = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False
class TestParkingSystem(unittest.TestCase):
    def test_example_1(self) -> None:
        ps = ParkingSystem(1, 1, 0)
        self.assertTrue(ps.addCar(1))
        self.assertTrue(ps.addCar(2))
        self.assertFalse(ps.addCar(3))
        self.assertFalse(ps.addCar(1))


if __name__ == "__main__":
    unittest.main()
