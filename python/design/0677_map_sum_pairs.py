"""
LeetCode 677: Map Sum Pairs
Difficulty: Medium
Tags: Hash Table, String, Design, Trie

--------------------------------------------------------------------------------
PROBLEM DESCRIPTION:
Design a map that allows you to do the following:
- Maps a string key to a given value.
- Returns the sum of the values that have a name with a prefix equal to a given string.

Implement the `MapSum` class:
- `MapSum()` Initializes the `MapSum` object.
- `void insert(String key, int val)` Inserts the `key-val` pair into the map. If the `key` already existed, the original `key-val` pair will be overridden to the new one.
- `int sum(String prefix)` Returns the sum of all the pairs' value whose key starts with the prefix.

--------------------------------------------------------------------------------
EXAMPLES:
Example 1:
Input:
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output:
[null, null, 3, null, 5]

Explanation:
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple=3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple=3, app=2)

--------------------------------------------------------------------------------
COMPLEXITY TARGETS:
Time Complexity:
- `insert`: O(L) where L is length of key.
- `sum`: O(P) where P is length of prefix.
Space Complexity: O(Total characters in keys).

--------------------------------------------------------------------------------
DESIGN INSIGHTS:
Use a Trie where each node stores `sum_val: int`.
Also keep a hash map `key_to_val: dict[str, int]`.
When inserting `(key, val)`:
- Compute `delta = val - key_to_val.get(key, 0)`.
- Update `key_to_val[key] = val`.
- Traverse Trie for `key`, adding `delta` to `node.sum_val` at every node.
`sum(prefix)` simply returns `node.sum_val` at the end of prefix in O(P) time!
"""

import unittest
class MapSumNode:
    def __init__(self) -> None:
        self.children: dict[str, MapSumNode] = {}
        self.sum_val: int = 0


class MapSum:
    """Prefix-sum Trie maintaining running subtree sums."""

    def __init__(self) -> None:
        self.root = MapSumNode()
        self.map: dict[str, int] = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val

        curr = self.root
        curr.sum_val += delta
        for char in key:
            if char not in curr.children:
                curr.children[char] = MapSumNode()
            curr = curr.children[char]
            curr.sum_val += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.sum_val
class TestMapSum(unittest.TestCase):
    def test_example_1(self) -> None:
        ms = MapSum()
        ms.insert("apple", 3)
        self.assertEqual(ms.sum("ap"), 3)
        ms.insert("app", 2)
        self.assertEqual(ms.sum("ap"), 5)


if __name__ == "__main__":
    unittest.main()
