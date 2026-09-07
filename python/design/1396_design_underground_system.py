"""
LeetCode 1396: Design Underground System
Difficulty: Medium
Tags: Hash Table, String, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the `UndergroundSystem` class:
- `void checkIn(int id, string stationName, int t)`
- `void checkOut(int id, string stationName, int t)`
- `double getAverageTime(string startStation, string endStation)` Returns the average time it takes to travel from `startStation` to `endStation`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
Output:
[null,null,null,null,null,null,null,14.0,11.0,null,11.0,null,12.0]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `checkIn`, `checkOut`, `getAverageTime`: O(1)
Space Complexity: O(Active passengers + Unique routes).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `check_ins: dict[id, (start_station, checkin_time)]`
- `route_stats: dict[(start_station, end_station), [total_time, trip_count]]`
When customer checks out:
- Retrieve `start_station, t0 = check_ins.pop(id)`
- Compute travel time `t - t0` and accumulate into `route_stats[(start_station, end_station)]`.
`getAverageTime` returns `total_time / trip_count` in O(1).
"""

import unittest
from collections import defaultdict


class UndergroundSystem:
    """Underground railway transit tracking and average journey time calculation."""

    def __init__(self) -> None:
        # id -> (stationName, timestamp)
        self.check_ins: dict[int, tuple[str, int]] = {}
        # (startStation, endStation) -> [total_time, count]
        self.route_stats: dict[tuple[str, str], list[int]] = defaultdict(
            lambda: [0, 0]
        )

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        route = (start_station, stationName)
        duration = t - start_time
        self.route_stats[route][0] += duration
        self.route_stats[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.route_stats[(startStation, endStation)]
        return total_time / count
class TestUndergroundSystem(unittest.TestCase):
    def test_example_1(self) -> None:
        us = UndergroundSystem()
        us.checkIn(45, "Leyton", 3)
        us.checkIn(32, "Paradise", 8)
        us.checkIn(27, "Leyton", 10)
        us.checkOut(45, "Waterloo", 15)
        us.checkOut(27, "Waterloo", 20)
        us.checkOut(32, "Cambridge", 22)
        self.assertAlmostEqual(us.getAverageTime("Paradise", "Cambridge"), 14.0, places=5)
        self.assertAlmostEqual(us.getAverageTime("Leyton", "Waterloo"), 11.0, places=5)


if __name__ == "__main__":
    unittest.main()
