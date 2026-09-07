"""
LeetCode 3885: Design Event Manager
Difficulty: Medium
Tags: Hash Table, Design, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design an event manager that allows registering events with priorities and polling the highest priority event.

Implement the `EventManager` class:
- `EventManager(List<List<Integer>> events)` Initializes with `[eventId, priority]`.
- `void updateEvent(int eventId, int priority)` Updates the priority of `eventId`.
- `int pollHighestPriority()` Removes and returns `eventId` of highest priority event (lowest eventId breaks ties). Returns `-1` if empty.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["EventManager", "updateEvent", "pollHighestPriority", "pollHighestPriority"]
[[[[1, 10], [2, 20]]], [1, 25], [], []]
Output:
[null, null, 1, 2]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `updateEvent`: O(log N)
- `pollHighestPriority`: O(log N) amortized
Space Complexity: O(N) for event map and max-heap.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `event_priorities: dict[eventId, priority]`
- `max_heap: list[(-priority, eventId)]`
On `pollHighestPriority()`:
Pop from heap until top priority matches recorded `event_priorities[eventId]`. Delete from map and return `eventId`.
"""

import unittest
import heapq


class EventManager:
    """Event priority scheduler with lazy heap updates."""

    def __init__(self, events: list[list[int]]) -> None:
        self.priorities: dict[int, int] = {}
        self.heap: list[tuple[int, int]] = []  # (-priority, eventId)

        for eid, p in events:
            self.updateEvent(eid, p)

    def updateEvent(self, eventId: int, priority: int) -> None:
        self.priorities[eventId] = priority
        heapq.heappush(self.heap, (-priority, eventId))

    def pollHighestPriority(self) -> int:
        while self.heap:
            neg_p, eid = heapq.heappop(self.heap)
            if eid in self.priorities and self.priorities[eid] == -neg_p:
                del self.priorities[eid]
                return eid
        return -1
class TestEventManager(unittest.TestCase):
    def test_example_1(self) -> None:
        em = EventManager([[1, 10], [2, 20]])
        em.updateEvent(1, 25)
        self.assertEqual(em.pollHighestPriority(), 1)
        self.assertEqual(em.pollHighestPriority(), 2)
        self.assertEqual(em.pollHighestPriority(), -1)


if __name__ == "__main__":
    unittest.main()
