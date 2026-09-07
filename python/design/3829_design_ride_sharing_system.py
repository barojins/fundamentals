"""
LeetCode 3829: Design Ride Sharing System
Difficulty: Medium
Tags: Hash Table, Design, Simulation

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a ride sharing dispatcher that tracks ride requests and fare computations.

Implement the `RideSharing` class:
- `RideSharing()`
- `void requestRide(int rideId, int passengerId, int pickup, int dropoff)`
- `bool matchDriver(int rideId, int driverId)`
- `int completeRide(int rideId)` Returns fare `(dropoff - pickup) * 10` upon completion.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["RideSharing", "requestRide", "matchDriver", "completeRide"]
[[], [1, 101, 10, 25], [1, 501], [1]]
Output:
[null, null, true, 150]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `requestRide`, `matchDriver`, `completeRide`: O(1)
Space Complexity: O(Active rides).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store per-ride record: `{ "passenger": int, "pickup": int, "dropoff": int, "driver": int, "status": str }`.
"""

import unittest
class RideSharing:
    """Ride dispatch and fare calculation system."""

    def __init__(self) -> None:
        self.rides: dict[int, dict] = {}

    def requestRide(
        self, rideId: int, passengerId: int, pickup: int, dropoff: int
    ) -> None:
        self.rides[rideId] = {
            "passenger": passengerId,
            "pickup": pickup,
            "dropoff": dropoff,
            "driver": None,
            "status": "REQUESTED",
        }

    def matchDriver(self, rideId: int, driverId: int) -> bool:
        if (
            rideId not in self.rides
            or self.rides[rideId]["status"] != "REQUESTED"
        ):
            return False
        self.rides[rideId]["driver"] = driverId
        self.rides[rideId]["status"] = "MATCHED"
        return True

    def completeRide(self, rideId: int) -> int:
        if rideId not in self.rides or self.rides[rideId]["status"] != "MATCHED":
            return -1
        ride = self.rides.pop(rideId)
        fare = (ride["dropoff"] - ride["pickup"]) * 10
        return fare
class TestRideSharing(unittest.TestCase):
    def test_example_1(self) -> None:
        rs = RideSharing()
        rs.requestRide(1, 101, 10, 25)
        self.assertTrue(rs.matchDriver(1, 501))
        self.assertEqual(rs.completeRide(1), 150)


if __name__ == "__main__":
    unittest.main()
