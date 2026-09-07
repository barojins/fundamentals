"""
LeetCode 432: All O`one Data Structure
Difficulty: Hard
Tags: Hash Table, Linked List, Doubly-Linked List, Design

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the `AllOne` class:
- `AllOne()` Initializes the object of the data structure.
- `inc(String key)` Increments the count of the string `key` by `1`. If `key` does not exist in the data structure, insert it with count `1`.
- `dec(String key)` Decrements the count of the string `key` by `1`. If the count of `key` reaches `0`, it is removed from the data structure. It is guaranteed that `key` exists in the data structure before the decrement.
- `getMaxKey()` Returns one of the keys with the maximal count. If no element exists, return an empty string `""`.
- `getMinKey()` Returns one of the keys with the minimum count. If no element exists, return an empty string `""`.

Notice that each function must run in `O(1)` average time complexity.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output:
[null, null, null, "hello", "hello", null, "hello", "leet"]

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `inc(key)`: O(1)
- `dec(key)`: O(1)
- `getMaxKey()`: O(1)
- `getMinKey()`: O(1)
Space Complexity: O(N) where N is the number of distinct keys.

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Doubly Linked List of `Bucket` nodes where each bucket stores a `count` and a `keys: set[str]`.
Buckets are sorted in strictly increasing order of `count`.
- Sentinel `head` (count = 0) and `tail` (count = inf).
- Map `key_to_bucket: dict[str, Bucket]`.
- `inc`: move `key` to bucket with `count + 1` (create if doesn't exist next to current bucket).
- `dec`: move `key` to bucket with `count - 1` (or delete if count becomes 0).
- `getMaxKey()`: return any key from `tail.prev.keys` if `tail.prev != head` else `""`.
- `getMinKey()`: return any key from `head.next.keys` if `head.next != tail` else `""`.
"""

import unittest


class Bucket:
    def __init__(self, count: int = 0) -> None:
        self.count: int = count
        self.keys: set[str] = set()
        self.prev: Bucket | None = None
        self.next: Bucket | None = None


class AllOne:
    """O(1) Data structure maintaining minimum and maximum string frequencies."""

    def __init__(self) -> None:
        self.head: Bucket = Bucket(0)  # Sentinel min
        self.tail: Bucket = Bucket(float("inf"))  # Sentinel max
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_bucket: dict[str, Bucket] = {}

    def _insert_after(self, prev_bucket: Bucket, new_bucket: Bucket) -> None:
        next_bucket = prev_bucket.next
        new_bucket.prev = prev_bucket
        new_bucket.next = next_bucket
        prev_bucket.next = new_bucket
        if next_bucket:
            next_bucket.prev = new_bucket

    def _remove_bucket(self, bucket: Bucket) -> None:
        prev_bucket = bucket.prev
        next_bucket = bucket.next
        if prev_bucket:
            prev_bucket.next = next_bucket
        if next_bucket:
            next_bucket.prev = prev_bucket

    def inc(self, key: str) -> None:
        if key not in self.key_bucket:
            if self.head.next.count == 1:
                self.head.next.keys.add(key)
                self.key_bucket[key] = self.head.next
            else:
                new_bucket = Bucket(1)
                new_bucket.keys.add(key)
                self._insert_after(self.head, new_bucket)
                self.key_bucket[key] = new_bucket
        else:
            cur_bucket = self.key_bucket[key]
            next_bucket = cur_bucket.next
            if next_bucket.count == cur_bucket.count + 1:
                next_bucket.keys.add(key)
                self.key_bucket[key] = next_bucket
            else:
                new_bucket = Bucket(cur_bucket.count + 1)
                new_bucket.keys.add(key)
                self._insert_after(cur_bucket, new_bucket)
                self.key_bucket[key] = new_bucket

            cur_bucket.keys.remove(key)
            if not cur_bucket.keys:
                self._remove_bucket(cur_bucket)

    def dec(self, key: str) -> None:
        if key not in self.key_bucket:
            return

        cur_bucket = self.key_bucket[key]
        if cur_bucket.count == 1:
            del self.key_bucket[key]
        else:
            prev_bucket = cur_bucket.prev
            if prev_bucket.count == cur_bucket.count - 1:
                prev_bucket.keys.add(key)
                self.key_bucket[key] = prev_bucket
            else:
                new_bucket = Bucket(cur_bucket.count - 1)
                new_bucket.keys.add(key)
                self._insert_after(prev_bucket, new_bucket)
                self.key_bucket[key] = new_bucket

        cur_bucket.keys.remove(key)
        if not cur_bucket.keys:
            self._remove_bucket(cur_bucket)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


class TestAllOne(unittest.TestCase):
    def test_example_1(self) -> None:
        ao = AllOne()
        ao.inc("hello")
        ao.inc("hello")
        self.assertEqual(ao.getMaxKey(), "hello")
        self.assertEqual(ao.getMinKey(), "hello")
        ao.inc("leet")
        self.assertEqual(ao.getMaxKey(), "hello")
        self.assertEqual(ao.getMinKey(), "leet")

    def test_empty_and_dec_to_zero(self) -> None:
        ao = AllOne()
        self.assertEqual(ao.getMaxKey(), "")
        self.assertEqual(ao.getMinKey(), "")
        ao.inc("a")
        ao.dec("a")
        self.assertEqual(ao.getMaxKey(), "")
        self.assertEqual(ao.getMinKey(), "")


if __name__ == "__main__":
    unittest.main()
