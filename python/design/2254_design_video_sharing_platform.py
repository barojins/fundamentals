"""
LeetCode 2254: Design Video Sharing Platform
Difficulty: Hard
Tags: Array, Hash Table, String, Design, Heap (Priority Queue)

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
You have a video sharing platform. Each video has a unique `videoId` which is the smallest positive integer not currently taken.

Implement the `VideoSharingPlatform` class:
- `VideoSharingPlatform()`
- `int upload(String video)`
- `void remove(int videoId)`
- `String watch(int videoId, int startMinute, int endMinute)` Increments view count, returns substring `video[startMinute : min(endMinute + 1, len(video))]`.
- `void like(int videoId)`
- `void dislike(int videoId)`
- `int[] getLikesAndDislikes(int videoId)` Returns `[likes, dislikes]`.
- `int getViews(int videoId)` Returns views count.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["VideoSharingPlatform","upload","upload","remove","remove","upload","watch","like","dislike","getLikesAndDislikes","getViews"]
[[],["abc"],["def"],[0],[1],["ghi"],[0,0,1],[0],[0],[0],[0]]
Output:
[null,0,1,null,null,0,"gh",null,null,[1,1],1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `upload`, `remove`: O(log V)
- `watch`: O(substring length)
- `like`, `dislike`, `getLikesAndDislikes`, `getViews`: O(1)
Space Complexity: O(Total videos content).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a min-heap `available_ids` and counter `next_id = 0` for ID assignment.
Store video metadata in `videos: dict[int, dict]`:
`{ "content": str, "views": int, "likes": int, "dislikes": int }`.
"""

import unittest
import heapq


class VideoSharingPlatform:
    """Video hosting, streaming, metrics, and ID recycling platform."""

    def __init__(self) -> None:
        self.available_ids: list[int] = []
        self.next_id: int = 0
        self.videos: dict[int, dict] = {}

    def upload(self, video: str) -> int:
        if self.available_ids:
            vid = heapq.heappop(self.available_ids)
        else:
            vid = self.next_id
            self.next_id += 1

        self.videos[vid] = {
            "content": video,
            "views": 0,
            "likes": 0,
            "dislikes": 0,
        }
        return vid

    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
            del self.videos[videoId]
            heapq.heappush(self.available_ids, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.videos:
            return "-1"
        v = self.videos[videoId]
        v["views"] += 1
        content = v["content"]
        return content[startMinute : min(endMinute + 1, len(content))]

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId]["likes"] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId]["dislikes"] += 1

    def getLikesAndDislikes(self, videoId: int) -> list[int]:
        if videoId not in self.videos:
            return [-1]
        v = self.videos[videoId]
        return [v["likes"], v["dislikes"]]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.videos:
            return -1
        return self.videos[videoId]["views"]
class TestVideoSharingPlatform(unittest.TestCase):
    def test_example_1(self) -> None:
        vsp = VideoSharingPlatform()
        self.assertEqual(vsp.upload("abc"), 0)
        self.assertEqual(vsp.upload("def"), 1)
        vsp.remove(0)
        vsp.remove(1)
        self.assertEqual(vsp.upload("ghi"), 0)
        self.assertEqual(vsp.watch(0, 0, 1), "gh")
        vsp.like(0)
        vsp.dislike(0)
        self.assertEqual(vsp.getLikesAndDislikes(0), [1, 1])
        self.assertEqual(vsp.getViews(0), 1)


if __name__ == "__main__":
    unittest.main()
