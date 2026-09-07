"""
LeetCode 1348: Tweet Counts Per Frequency
Difficulty: Medium
Tags: Hash Table, Binary Search, Design, Sorting, Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur over certain periods of time.

Implement the `TweetCounts` class:
- `TweetCounts()` Initializes the `TweetCounts` object.
- `void recordTweet(String tweetName, int time)` Stores the `tweetName` at the recorded `time` (in seconds).
- `List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime)` Returns a list of integers representing the number of tweets with `tweetName` in each time interval for the given frequency `freq` (which can be `"minute"`, `"hour"`, or `"day"`).
  - `"minute"`: 60 seconds interval chunk
  - `"hour"`: 3600 seconds interval chunk
  - `"day"`: 86400 seconds interval chunk

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
Output:
[null,null,null,null,[2],[2,1],null,[4]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `recordTweet`: O(1) (or O(log N) sorted insertion)
- `getTweetCountsPerFrequency`: O(N + total_chunks)
Space Complexity: O(T) for stored tweets.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Map `freq` string to bucket delta:
- `minute`: 60
- `hour`: 3600
- `day`: 86400
Compute number of chunks: `(endTime - startTime) // delta + 1`.
Filter timestamps `startTime <= t <= endTime`, and place into chunk `(t - startTime) // delta`.
"""

import unittest
from collections import defaultdict


class TweetCounts:
    """Aggregates tweet frequency counts across minute, hour, or day buckets."""

    FREQ_DELTAS = {"minute": 60, "hour": 3600, "day": 86400}

    def __init__(self) -> None:
        self.tweets: dict[str, list[int]] = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> list[int]:
        delta = self.FREQ_DELTAS[freq]
        num_buckets = (endTime - startTime) // delta + 1
        res = [0] * num_buckets

        for t in self.tweets.get(tweetName, []):
            if startTime <= t <= endTime:
                bucket_idx = (t - startTime) // delta
                res[bucket_idx] += 1

        return res
class TestTweetCounts(unittest.TestCase):
    def test_example_1(self) -> None:
        tc = TweetCounts()
        tc.recordTweet("tweet3", 0)
        tc.recordTweet("tweet3", 60)
        tc.recordTweet("tweet3", 10)
        self.assertEqual(tc.getTweetCountsPerFrequency("minute", "tweet3", 0, 59), [2])
        self.assertEqual(tc.getTweetCountsPerFrequency("minute", "tweet3", 0, 60), [2, 1])
        tc.recordTweet("tweet3", 120)
        self.assertEqual(tc.getTweetCountsPerFrequency("hour", "tweet3", 0, 210), [4])


if __name__ == "__main__":
    unittest.main()
