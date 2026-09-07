"""
LeetCode 1500: Design a File Sharing System
Difficulty: Medium
Tags: Hash Table, Design, Heap (Priority Queue), Ordered Set

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
We will use a file-sharing system to share a very large file which consists of `m` small chunks with IDs from `1` to `m`.

When users join the system, the system should assign a unique ID to them. The unique ID should be the smallest positive integer that is not currently taken.

Implement the `FileSharing` class:
- `FileSharing(int m)` Initializes the object with a file of `m` chunks.
- `int join(int[] ownedChunks)` A new user joined the system owning some chunks of the file, returns the assigned user ID.
- `void leave(int userID)` The user with `userID` left the system, releasing all owned chunks.
- `int[] request(int userID, int chunkID)` The user with `userID` requested the chunk with `chunkID`. Returns a list of the IDs of all users that own this chunk sorted in ascending order. If the chunk is successfully received (at least one other user owns it), the user also owns `chunkID` from now on.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["FileSharing","join","join","join","request","request","leave","request","leave","join"]
[[4],[[1,2]],[[2,3]],[[4]],[1,3],[2,2],[1],[2,1],[2],[[]]]
Output:
[null,1,2,3,[2],[1,2],null,[],null,1]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `join`: O(log U)
- `leave`: O(C) where C is number of owned chunks.
- `request`: O(U log U) to find and sort owners.
Space Complexity: O(U * C) for chunk ownership maps.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Track reusable user IDs using a min-heap `available_ids` and max assigned ID `max_id`.
Maintain:
- `user_chunks: dict[userID, set[int]]`
- `chunk_users: dict[chunkID, set[int]]`
On `request(userID, chunkID)`:
- Retrieve `owners = sorted(chunk_users[chunkID])`.
- If `owners`: `user_chunks[userID].add(chunkID)` and `chunk_users[chunkID].add(userID)`.
"""

import unittest
from collections import defaultdict
import heapq


class FileSharing:
    """P2P File Sharing chunk registry with recycling user IDs."""

    def __init__(self, m: int) -> None:
        self.m: int = m
        self.available_ids: list[int] = []
        self.max_id: int = 0
        self.user_chunks: dict[int, set[int]] = defaultdict(set)
        self.chunk_users: dict[int, set[int]] = defaultdict(set)

    def join(self, ownedChunks: list[int]) -> int:
        if self.available_ids:
            user_id = heapq.heappop(self.available_ids)
        else:
            self.max_id += 1
            user_id = self.max_id

        self.user_chunks[user_id] = set(ownedChunks)
        for chunk in ownedChunks:
            self.chunk_users[chunk].add(user_id)

        return user_id

    def leave(self, userID: int) -> None:
        if userID in self.user_chunks:
            for chunk in self.user_chunks[userID]:
                self.chunk_users[chunk].discard(userID)
            del self.user_chunks[userID]
            heapq.heappush(self.available_ids, userID)

    def request(self, userID: int, chunkID: int) -> list[int]:
        owners = sorted(self.chunk_users[chunkID])
        if owners:
            self.user_chunks[userID].add(chunkID)
            self.chunk_users[chunkID].add(userID)
        return owners
class TestFileSharing(unittest.TestCase):
    def test_example_1(self) -> None:
        fs = FileSharing(4)
        u1 = fs.join([1, 2])
        u2 = fs.join([2, 3])
        u3 = fs.join([4])
        self.assertEqual(u1, 1 and u2 == 2 and u3 == 3)
        self.assertEqual(fs.request(1, 3), [2])
        self.assertEqual(fs.request(2, 2), [1, 2])
        fs.leave(1)
        self.assertEqual(fs.request(2, 1), [])
        fs.leave(2)
        u_new = fs.join([])
        self.assertEqual(u_new, 1)


if __name__ == "__main__":
    unittest.main()
