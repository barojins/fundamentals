import * as templates from "./templates.ts";

function assert(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}

function equal(actual: unknown, expected: unknown, message: string): void {
  assert(JSON.stringify(actual) === JSON.stringify(expected), message);
}

const numbers = [1, 2, 4, 6] as const;
equal(
  [...templates.frequencies(["a", "b", "a"] as const)],
  [
    ["a", 2],
    ["b", 1],
  ],
  "frequency map",
);
equal(templates.twoSumSorted(numbers, 8), [1, 3], "two pointers");
assert(templates.maxWindowSum([2, 1, 5, 1, 3, 2] as const, 3) === 9, "fixed window");
assert(templates.longestUniqueSubstring("😀a😀") === 2, "variable window");
const prefix = templates.prefixSums([2, 4, 1, 3] as const);
assert(templates.rangeSum(prefix, 1, 3) === 8, "prefix sum");
assert(templates.maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4] as const) === 6, "Kadane");
assert(templates.binarySearch([1, 3, 5, 7] as const, 5) === 2, "binary search");
equal(templates.nextGreater([2, 1, 2, 4, 3] as const), [4, 2, 4, -1, -1], "stack");

const head = new templates.ListNode(1, new templates.ListNode(2, new templates.ListNode(3)));
head.value = 10;
const reversed = templates.reverseList(head);
const reversedValues: number[] = [];
for (let node = reversed; node; node = node.next) reversedValues.push(node.value);
equal(reversedValues, [3, 2, 10], "linked-list reversal");
assert(!templates.hasCycle(reversed), "acyclic list");
const cycle = new templates.ListNode(1, new templates.ListNode(2));
if (!cycle.next) throw new Error("cycle fixture");
cycle.next.next = cycle;
assert(templates.hasCycle(cycle), "cycle detection");

const graph = new Map([
  ["A", ["B", "C"] as const],
  ["B", ["D"] as const],
  ["C", ["D"] as const],
  ["D", [] as const],
]);
equal(templates.dfsRecursive(graph, "A"), ["A", "B", "D", "C"], "recursive DFS");
equal(templates.dfsIterative(graph, "A"), ["A", "B", "D", "C"], "iterative DFS");
equal(templates.bfs(graph, "A"), ["A", "B", "C", "D"], "BFS");

const weighted = new Map([
  [
    1,
    [
      [2, 4],
      [3, 1],
    ] as const,
  ],
  [3, [[2, 2]] as const],
  [2, [] as const],
]);
const distances = templates.dijkstra(weighted, 1);
assert(distances.get(1) === 0 && distances.get(2) === 3 && distances.get(3) === 1, "Dijkstra");

equal(templates.subsets([1, 2] as const), [[], [2], [1], [1, 2]], "backtracking");
equal(templates.topK([3, 1, 5, 2, 4] as const, 3), [5, 4, 3], "top K");
equal(
  templates.mergeIntervals([
    [1, 3],
    [2, 6],
    [8, 10],
  ] as const),
  [
    [1, 6],
    [8, 10],
  ],
  "intervals",
);
assert(templates.coinChange([1, 2, 5] as const, 11) === 3, "coin change");

const sparse: number[] = [];
sparse.length = 1;
let rejectedSparseInput = false;
try {
  templates.binarySearch(sparse, 1);
} catch (error) {
  rejectedSparseInput = error instanceof RangeError;
}
assert(rejectedSparseInput, "sparse arrays must be rejected");

for (const [coins, amount] of [
  [[1], -1],
  [[0, 1], 3],
  [[-1, 2], 3],
] as const) {
  let threw = false;
  try {
    templates.coinChange(coins, amount);
  } catch {
    threw = true;
  }
  assert(threw, "invalid coin-change input");
}

console.log("TypeScript: all template tests passed");
