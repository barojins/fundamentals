"""
LeetCode 635: Design Log Storage System
Difficulty: Medium
Tags: Hash Table, String, Design, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You are given several logs, where each log contains a unique ID and timestamp. Timestamp is a string that has the following format: `Year:Month:Day:Hour:Minute:Second`, for example, `2017:01:01:23:59:59`. All domains are zero-padded decimal numbers.

Implement the `LogSystem` class:
- `LogSystem()` Initializes the `LogSystem` object.
- `void put(int id, string timestamp)` Stores the given log `(id, timestamp)` in the storage system.
- `int[] retrieve(string start, string end, string granularity)` Returns the IDs of the logs whose timestamps are within the range from `start` to `end` inclusive according to the specified `granularity`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
Output:
[null, null, null, null, [3, 2, 1], [2, 1]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `put`: O(1)
- `retrieve`: O(N) where N is number of stored logs.
Space Complexity: O(N) to store logs.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map granularity to prefix substring length:
- `Year`: 4 (`YYYY`)
- `Month`: 7 (`YYYY:MM`)
- `Day`: 10 (`YYYY:MM:DD`)
- `Hour`: 13 (`YYYY:MM:DD:HH`)
- `Minute`: 16 (`YYYY:MM:DD:HH:MM`)
- `Second`: 19 (`YYYY:MM:DD:HH:MM:SS`)
Truncate `timestamp[:idx]` and filter `start[:idx] <= timestamp[:idx] <= end[:idx]`.
"""

import unittest
class LogSystem:
    """Log storage and retrieval with variable time granularity."""

    GRANULARITY_INDICES = {
        "Year": 4,
        "Month": 7,
        "Day": 10,
        "Hour": 13,
        "Minute": 16,
        "Second": 19,
    }

    def __init__(self) -> None:
        self.logs: list[tuple[int, str]] = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> list[int]:
        idx = self.GRANULARITY_INDICES[granularity]
        start_pref = start[:idx]
        end_pref = end[:idx]

        res = []
        for log_id, timestamp in self.logs:
            if start_pref <= timestamp[:idx] <= end_pref:
                res.append(log_id)
        return res

class TestLogSystem(unittest.TestCase):
    def test_example_1(self) -> None:
        logs = LogSystem()
        logs.put(1, "2017:01:01:23:59:59")
        logs.put(2, "2017:01:01:22:59:59")
        logs.put(3, "2016:01:01:00:00:00")
        self.assertEqual(
            sorted(logs.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")),
            [1, 2, 3],
        )
        self.assertEqual(
            sorted(logs.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")),
            [1, 2],
        )


if __name__ == "__main__":
    unittest.main()
