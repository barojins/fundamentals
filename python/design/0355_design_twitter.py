"""
LeetCode 355: Design Twitter
Difficulty: Medium
Tags: Hash Table, Linked List, Design, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.

Implement the `Twitter` class:
- `Twitter()` Initializes your twitter object.
- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID `tweetId` by the user `userId`. Each call to this function will be made with a unique `tweetId`.
- `List<Integer> getNewsFeed(int userId)` Retrieves the `10` most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- `void follow(int followerId, int followeeId)` The user with ID `followerId` started following the user with ID `followeeId`.
- `void unfollow(int followerId, int followeeId)` The user with ID `followerId` unfollowed the user with ID `followeeId`.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output:
[null, null, [5], null, null, [6, 5], null, [5]]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `postTweet`: O(1)
- `getNewsFeed`: O(F log F) or O(10 log F) where F is followees count via k-way merge
- `follow` / `unfollow`: O(1)
Space Complexity: O(Users + Tweets).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Maintain:
- `self.time`: Monotonic counter for chronological ordering.
- `self.tweets: dict[int, list[tuple[int, int]]]`: user -> list of `(timestamp, tweetId)`
- `self.following: dict[int, set[int]]`: user -> set of followee IDs
When generating feed:
- Merge tweets from `self.following[userId] | {userId}` using `heapq.merge` or max-heap, taking up to 10 most recent.
"""

import heapq
import unittest


class Twitter:
    """Simplified Twitter with post, follow/unfollow, and 10-most-recent feed."""

    def __init__(self) -> None:
        self.time: int = 0
        self.tweets: dict[int, list[tuple[int, int]]] = {}
        self.following: dict[int, set[int]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        users = set(self.following.get(userId, set()))
        users.add(userId)

        # Max heap by negating timestamp: (-time, tweetId, user, next_idx)
        heap: list[tuple[int, int, int, int]] = []
        for u in users:
            if u in self.tweets and self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                t, tid = self.tweets[u][idx]
                heap.append((-t, tid, u, idx))

        heapq.heapify(heap)
        feed: list[int] = []

        while heap and len(feed) < 10:
            neg_t, tid, u, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                next_idx = idx - 1
                nt, ntid = self.tweets[u][next_idx]
                heapq.heappush(heap, (-nt, ntid, u, next_idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


class TestTwitter(unittest.TestCase):
    def test_example_1(self) -> None:
        t = Twitter()
        t.postTweet(1, 5)
        self.assertEqual(t.getNewsFeed(1), [5])
        t.follow(1, 2)
        t.postTweet(2, 6)
        self.assertEqual(t.getNewsFeed(1), [6, 5])
        t.unfollow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [5])

    def test_feed_limit_10(self) -> None:
        t = Twitter()
        for i in range(15):
            t.postTweet(1, i)
        feed = t.getNewsFeed(1)
        self.assertEqual(len(feed), 10)
        self.assertEqual(feed, list(range(14, 4, -1)))

    def test_unfollow_nonexistent_or_self(self) -> None:
        t = Twitter()
        t.unfollow(1, 2)  # Should not raise exception
        t.postTweet(1, 10)
        self.assertEqual(t.getNewsFeed(1), [10])


if __name__ == "__main__":
    unittest.main()
