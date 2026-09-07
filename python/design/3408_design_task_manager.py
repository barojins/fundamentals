"""
LeetCode 3408: Design Task Manager
Difficulty: Medium
Tags: Hash Table, Design, Heap (Priority Queue), Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
There is a task management system that allows users to manage tasks with priorities.

Implement the `TaskManager` class:
- `TaskManager(List<List<Integer>> tasks)` Initializes with `tasks` where `tasks[i] = [userId, taskId, priority]`.
- `void add(int userId, int taskId, int priority)` Adds a task.
- `void edit(int taskId, int newPriority)` Updates the priority of `taskId`.
- `void rmv(int taskId)` Removes `taskId`.
- `int execTop()` Executes and removes the highest priority task (breaking ties with highest taskId), returns its `userId` or `-1` if empty.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
Output:
[null, null, null, 3, null, null, 5]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `add`, `edit`, `rmv`: O(log N)
- `execTop`: O(log N) amortized
Space Complexity: O(N) for max-heap and task map.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `task_info: dict[taskId, (userId, priority)]`
- `max_heap: list[(-priority, -taskId, userId)]`
On `execTop()`:
Pop from heap until top matches current recorded `task_info[taskId]`. Delete and return `userId`.
"""

import unittest
import heapq


class TaskManager:
    """Priority task manager with lazy deletion max-heap."""

    def __init__(self, tasks: list[list[int]]) -> None:
        self.task_info: dict[int, tuple[int, int]] = {}  # taskId -> (userId, priority)
        self.heap: list[tuple[int, int, int]] = []  # (-priority, -taskId, userId)

        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_info:
            userId, _ = self.task_info[taskId]
            self.task_info[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.heap:
            neg_p, neg_t, u = heapq.heappop(self.heap)
            taskId = -neg_t
            p = -neg_p
            if taskId in self.task_info and self.task_info[taskId] == (u, p):
                del self.task_info[taskId]
                return u
        return -1
class TestTaskManager(unittest.TestCase):
    def test_example_1(self) -> None:
        tm = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
        tm.add(4, 104, 5)
        tm.edit(102, 8)
        self.assertEqual(tm.execTop(), 3)
        tm.rmv(101)
        tm.add(5, 105, 15)
        self.assertEqual(tm.execTop(), 5)


if __name__ == "__main__":
    unittest.main()
