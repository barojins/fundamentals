"""
LeetCode 3709: Design Exam Scores Tracker
Difficulty: Medium
Tags: Array, Hash Table, Design, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a tracker for student exam scores across multiple exams.

Implement the `ExamTracker` class:
- `ExamTracker()`
- `void recordScore(int studentId, int examId, int score)`
- `double getStudentAverage(int studentId)`
- `int getTopStudent(int examId)` Returns student with highest score on `examId` (lowest studentId breaks ties).

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["ExamTracker", "recordScore", "recordScore", "getStudentAverage", "getTopStudent"]
[[], [1, 101, 90], [1, 102, 80], [1], [101]]
Output:
[null, null, null, 85.0, 1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `recordScore`: O(1)
- `getStudentAverage`: O(1)
- `getTopStudent`: O(1)
Space Complexity: O(Scores recorded).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `student_scores: dict[studentId, list[score]]`
- `exam_top: dict[examId, (max_score, min_studentId)]`
"""

import unittest
from collections import defaultdict


class ExamTracker:
    """Exam scores tracker computing student averages and exam toppers."""

    def __init__(self) -> None:
        self.student_totals: dict[int, list[int]] = defaultdict(list)
        self.exam_topper: dict[int, tuple[int, int]] = {}  # examId -> (score, studentId)

    def recordScore(self, studentId: int, examId: int, score: int) -> None:
        self.student_totals[studentId].append(score)

        if examId not in self.exam_topper:
            self.exam_topper[examId] = (score, studentId)
        else:
            best_score, best_student = self.exam_topper[examId]
            if score > best_score or (score == best_score and studentId < best_student):
                self.exam_topper[examId] = (score, studentId)

    def getStudentAverage(self, studentId: int) -> float:
        scores = self.student_totals[studentId]
        return sum(scores) / len(scores)

    def getTopStudent(self, examId: int) -> int:
        return self.exam_topper[examId][1]
class TestExamTracker(unittest.TestCase):
    def test_example_1(self) -> None:
        et = ExamTracker()
        et.recordScore(1, 101, 90)
        et.recordScore(1, 102, 80)
        self.assertEqual(et.getStudentAverage(1), 85.0)
        self.assertEqual(et.getTopStudent(101), 1)


if __name__ == "__main__":
    unittest.main()
