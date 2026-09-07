"""
LeetCode 359: Logger Rate Limiter
Difficulty: Easy
Tags: Hash Table, Design, Data Stream

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most once every 10 seconds (i.e. a message printed at timestamp `t` will prevent other identical messages from being printed until timestamp `t + 10`).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the `Logger` class:
- `Logger()` Initializes the logger object.
- `bool shouldPrintMessage(int timestamp, string message)` Returns `true` if the `message` should be printed in the given `timestamp`, otherwise returns `false`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output:
[null, true, true, false, false, false, true]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `shouldPrintMessage`: O(1)
Space Complexity: O(M) where M is the number of distinct messages.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain a hash map `msg_to_next_valid_time: dict[str, int]`.
When `shouldPrintMessage(timestamp, message)` is called:
- If `timestamp < msg_to_next_valid_time.get(message, 0)`, return `False`.
- Otherwise update `msg_to_next_valid_time[message] = timestamp + 10` and return `True`.
"""

import unittest


class Logger:
    """Rate limiter ensuring identical messages are printed at most once every 10 seconds."""

    def __init__(self) -> None:
        self.msg_dict: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.msg_dict.get(message, 0):
            return False
        self.msg_dict[message] = timestamp + 10
        return True


class TestLogger(unittest.TestCase):
    def test_example_1(self) -> None:
        logger = Logger()
        self.assertTrue(logger.shouldPrintMessage(1, "foo"))
        self.assertTrue(logger.shouldPrintMessage(2, "bar"))
        self.assertFalse(logger.shouldPrintMessage(3, "foo"))
        self.assertFalse(logger.shouldPrintMessage(8, "bar"))
        self.assertFalse(logger.shouldPrintMessage(10, "foo"))
        self.assertTrue(logger.shouldPrintMessage(11, "foo"))

    def test_same_timestamp_different_messages(self) -> None:
        logger = Logger()
        self.assertTrue(logger.shouldPrintMessage(5, "a"))
        self.assertTrue(logger.shouldPrintMessage(5, "b"))
        self.assertFalse(logger.shouldPrintMessage(5, "a"))


if __name__ == "__main__":
    unittest.main()
