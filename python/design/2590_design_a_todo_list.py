"""
LeetCode 2590: Design a Todo List
Difficulty: Medium
Tags: Array, Hash Table, String, Design, Sorting

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a Todo List Where users can add tasks, mark them as complete, or get a list of uncompleted tasks.

Implement the `TodoList` class:
- `TodoList()`
- `int addTask(int userId, String taskDescription, int dueDate, List<String> tags)`
- `List<String> getAllTasks(int userId)` Returns uncompleted task descriptions sorted by dueDate ascending.
- `List<String> getTasksForTag(int userId, String tag)` Returns uncompleted tasks with `tag` sorted by dueDate ascending.
- `void completeTask(int userId, int taskId)`

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TodoList", "addTask", "addTask", "getAllTasks", "getAllTasks", "addTask", "getTasksForTag", "completeTask", "completeTask", "getTasksForTag", "getAllTasks"]
[[], [1, "Task1", 50, []], [1, "Task2", 100, ["tag1"]], [1], [5], [1, "Task3", 30, ["tag1"]], [1, "tag1"], [5, 1], [1, 2], [1, "tag1"], [1]]
Output:
[null, 1, 2, ["Task1", "Task2"], [], 3, ["Task3", "Task2"], null, null, ["Task3"], ["Task3", "Task1"]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `addTask`: O(1)
- `completeTask`: O(1)
- `getAllTasks`, `getTasksForTag`: O(T log T) sorting user tasks by due date.
Space Complexity: O(T) to store task records.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Store tasks per user in `user_tasks: dict[int, dict[int, Task]]`.
Task object has `taskId`, `desc`, `dueDate`, `tags: set[str]`.
`completeTask` deletes task from user map.
Queries filter and sort active tasks by `(dueDate, taskId)`.
"""

import unittest
from collections import defaultdict


class Task:
    def __init__(
        self, task_id: int, desc: str, due_date: int, tags: list[str]
    ) -> None:
        self.id: int = task_id
        self.desc: str = desc
        self.due_date: int = due_date
        self.tags: set[str] = set(tags)


class TodoList:
    """User task manager with tag filtering and due-date sorting."""

    def __init__(self) -> None:
        self.next_task_id: int = 1
        self.tasks: dict[int, dict[int, Task]] = defaultdict(dict)

    def addTask(
        self,
        userId: int,
        taskDescription: str,
        dueDate: int,
        tags: list[str],
    ) -> int:
        tid = self.next_task_id
        self.next_task_id += 1
        self.tasks[userId][tid] = Task(tid, taskDescription, dueDate, tags)
        return tid

    def getAllTasks(self, userId: int) -> list[str]:
        active_tasks = list(self.tasks[userId].values())
        active_tasks.sort(key=lambda t: (t.due_date, t.id))
        return [t.desc for t in active_tasks]

    def getTasksForTag(self, userId: int, tag: str) -> list[str]:
        active_tasks = [
            t for t in self.tasks[userId].values() if tag in self.tags_of(t)
        ]
        active_tasks.sort(key=lambda t: (t.due_date, t.id))
        return [t.desc for t in active_tasks]

    def tags_of(self, task: Task) -> set[str]:
        return task.tags

    def completeTask(self, userId: int, taskId: int) -> None:
        if taskId in self.tasks[userId]:
            del self.tasks[userId][taskId]
class TestTodoList(unittest.TestCase):
    def test_example_1(self) -> None:
        todo = TodoList()
        self.assertEqual(todo.addTask(1, "Task1", 50, []), 1)
        self.assertEqual(todo.addTask(1, "Task2", 100, ["tag1"]), 2)
        self.assertEqual(todo.getAllTasks(1), ["Task1", "Task2"])
        self.assertEqual(todo.getAllTasks(5), [])
        self.assertEqual(todo.addTask(1, "Task3", 30, ["tag1"]), 3)
        self.assertEqual(todo.getTasksForTag(1, "tag1"), ["Task3", "Task2"])
        todo.completeTask(5, 1)
        todo.completeTask(1, 2)
        self.assertEqual(todo.getTasksForTag(1, "tag1"), ["Task3"])
        self.assertEqual(todo.getAllTasks(1), ["Task3", "Task1"])


if __name__ == "__main__":
    unittest.main()
