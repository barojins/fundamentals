/** Compact coding-interview templates. */

function itemAt<T>(items: readonly T[], index: number): T {
  if (!Number.isInteger(index) || index < 0 || index >= items.length || !(index in items)) {
    throw new RangeError("index out of bounds");
  }
  return items[index] as T;
}

function popLast<T>(items: T[]): T {
  if (items.length === 0) throw new RangeError("cannot pop an empty array");
  return items.pop() as T;
}

function swap<T>(items: T[], left: number, right: number): void {
  const leftValue = itemAt(items, left);
  items[left] = itemAt(items, right);
  items[right] = leftValue;
}

// Frequency map — O(n) time, O(n) space
export function frequencies<T>(items: Iterable<T>): Map<T, number> {
  const counts = new Map<T, number>();
  for (const item of items) counts.set(item, (counts.get(item) ?? 0) + 1);
  return counts;
}

// Two pointers (sorted input) — O(n) time, O(1) space
export function twoSumSorted(nums: readonly number[], target: number): [number, number] | null {
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    const total = itemAt(nums, left) + itemAt(nums, right);
    if (total === target) return [left, right];
    total < target ? left++ : right--;
  }
  return null;
}

// Fixed sliding window — O(n) time, O(1) space
export function maxWindowSum(nums: readonly number[], k: number): number {
  if (k <= 0 || k > nums.length) throw new Error("k must be between 1 and nums.length");
  let window = 0;
  for (let index = 0; index < k; index++) window += itemAt(nums, index);
  let best = window;
  for (let right = k; right < nums.length; right++) {
    window += itemAt(nums, right) - itemAt(nums, right - k);
    best = Math.max(best, window);
  }
  return best;
}

// Variable sliding window — O(n) time, O(n) space
export function longestUniqueSubstring(text: string): number {
  const chars = Array.from(text);
  const lastSeen = new Map<string, number>();
  let left = 0;
  let best = 0;
  for (let right = 0; right < chars.length; right++) {
    const char = itemAt(chars, right);
    left = Math.max(left, (lastSeen.get(char) ?? -1) + 1);
    lastSeen.set(char, right);
    best = Math.max(best, right - left + 1);
  }
  return best;
}

// Prefix sum — build O(n), range query O(1)
export function prefixSums(nums: readonly number[]): number[] {
  const prefix = [0];
  for (const num of nums) prefix.push(itemAt(prefix, prefix.length - 1) + num);
  return prefix;
}

export function rangeSum(prefix: readonly number[], left: number, right: number): number {
  return itemAt(prefix, right + 1) - itemAt(prefix, left);
}

// Kadane's algorithm — O(n) time, O(1) space
export function maxSubarray(nums: readonly number[]): number {
  if (nums.length === 0) throw new Error("nums must not be empty");
  let current = itemAt(nums, 0);
  let best = current;
  for (let index = 1; index < nums.length; index++) {
    const num = itemAt(nums, index);
    current = Math.max(num, current + num);
    best = Math.max(best, current);
  }
  return best;
}

// Binary search — O(log n) time, O(1) space
export function binarySearch(nums: readonly number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;
  while (left <= right) {
    const middle = Math.floor((left + right) / 2);
    const value = itemAt(nums, middle);
    if (value === target) return middle;
    if (value < target) left = middle + 1;
    else right = middle - 1;
  }
  return -1;
}

export class ListNode {
  value: number;
  next: ListNode | null;

  constructor(value: number, next: ListNode | null = null) {
    this.value = value;
    this.next = next;
  }
}

// Linked-list reversal — O(n) time, O(1) space
export function reverseList(head: ListNode | null): ListNode | null {
  let previous: ListNode | null = null;
  while (head) {
    const following = head.next;
    head.next = previous;
    previous = head;
    head = following;
  }
  return previous;
}

// Fast and slow pointers (cycle detection) — O(n) time, O(1) space
export function hasCycle(head: ListNode | null): boolean {
  let slow = head;
  let fast = head;
  while (fast?.next) {
    if (slow === null) return false;
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}

// Monotonic stack (next greater value) — O(n) time, O(n) space
export function nextGreater(nums: readonly number[]): number[] {
  const answer = Array(nums.length).fill(-1);
  const stack: number[] = [];
  nums.forEach((num, index) => {
    while (stack.length && itemAt(nums, itemAt(stack, stack.length - 1)) < num) {
      answer[popLast(stack)] = num;
    }
    stack.push(index);
  });
  return answer;
}

export type Graph<T> = ReadonlyMap<T, readonly T[]>;

// Recursive DFS — O(V + E) time, O(V) space
export function dfsRecursive<T>(graph: Graph<T>, start: T): T[] {
  const order: T[] = [];
  const seen = new Set<T>();
  const visit = (node: T): void => {
    if (seen.has(node)) return;
    seen.add(node);
    order.push(node);
    for (const neighbor of graph.get(node) ?? []) visit(neighbor);
  };
  visit(start);
  return order;
}

// Iterative DFS — O(V + E) time, O(V + E) space
export function dfsIterative<T>(graph: Graph<T>, start: T): T[] {
  const order: T[] = [];
  const seen = new Set<T>();
  const stack = [start];
  while (stack.length) {
    const node = popLast(stack);
    if (seen.has(node)) continue;
    seen.add(node);
    order.push(node);
    stack.push(...[...(graph.get(node) ?? [])].reverse());
  }
  return order;
}

// BFS — O(V + E) time, O(V) space
export function bfs<T>(graph: Graph<T>, start: T): T[] {
  const order: T[] = [];
  const seen = new Set<T>([start]);
  const queue = [start];
  for (let front = 0; front < queue.length; front++) {
    const node = itemAt(queue, front);
    order.push(node);
    for (const neighbor of graph.get(node) ?? []) {
      if (!seen.has(neighbor)) {
        seen.add(neighbor);
        queue.push(neighbor);
      }
    }
  }
  return order;
}

// Backtracking (all subsets) — O(n * 2^n) time, O(n) recursion space
export function subsets(nums: readonly number[]): number[][] {
  const answer: number[][] = [];
  const path: number[] = [];
  const backtrack = (index: number): void => {
    if (index === nums.length) {
      answer.push([...path]);
      return;
    }
    backtrack(index + 1);
    path.push(itemAt(nums, index));
    backtrack(index + 1);
    path.pop();
  };
  backtrack(0);
  return answer;
}

class MinHeap<T> {
  private data: T[] = [];
  private readonly less: (a: T, b: T) => boolean;

  constructor(less: (a: T, b: T) => boolean) {
    this.less = less;
  }

  get size(): number {
    return this.data.length;
  }

  push(value: T): void {
    this.data.push(value);
    for (let child = this.data.length - 1; child > 0;) {
      const parent = Math.floor((child - 1) / 2);
      if (!this.less(itemAt(this.data, child), itemAt(this.data, parent))) break;
      swap(this.data, child, parent);
      child = parent;
    }
  }

  pop(): T | undefined {
    if (!this.data.length) return undefined;
    const root = itemAt(this.data, 0);
    const last = popLast(this.data);
    if (this.data.length) {
      this.data[0] = last;
      for (let parent = 0; ;) {
        let child = parent * 2 + 1;
        if (child >= this.data.length) break;
        if (
          child + 1 < this.data.length &&
          this.less(itemAt(this.data, child + 1), itemAt(this.data, child))
        )
          child++;
        if (!this.less(itemAt(this.data, child), itemAt(this.data, parent))) break;
        swap(this.data, child, parent);
        parent = child;
      }
    }
    return root;
  }

  peek(): T | undefined {
    return this.data.at(0);
  }
}

// Heap / top K — O(n log k) time, O(k) space
export function topK(nums: readonly number[], k: number): number[] {
  const heap = new MinHeap<number>((a, b) => a < b);
  for (const num of nums) {
    heap.push(num);
    if (heap.size > k) heap.pop();
  }
  const answer: number[] = [];
  while (heap.size) answer.push(heap.pop() as number);
  return answer.reverse();
}

// Merge intervals — O(n log n) time, O(n) space
export type Interval = readonly [start: number, end: number];

export function mergeIntervals(intervals: readonly Interval[]): [number, number][] {
  const merged: [number, number][] = [];
  for (const [start, end] of [...intervals].sort((a, b) => a[0] - b[0])) {
    const previous = merged.at(-1);
    if (!previous || start > previous[1]) merged.push([start, end]);
    else previous[1] = Math.max(previous[1], end);
  }
  return merged;
}

// Dijkstra (non-negative weights) — O((V + E) log V) time
export type WeightedGraph<T> = ReadonlyMap<T, ReadonlyArray<readonly [T, number]>>;

export function dijkstra<T>(graph: WeightedGraph<T>, start: T): Map<T, number> {
  const distances = new Map<T, number>([[start, 0]]);
  const heap = new MinHeap<[number, T]>((a, b) => a[0] < b[0]);
  heap.push([0, start]);
  while (heap.size) {
    const entry = heap.pop();
    if (!entry) break;
    const [distance, node] = entry;
    if (distance !== distances.get(node)) continue;
    for (const [neighbor, weight] of graph.get(node) ?? []) {
      const candidate = distance + weight;
      if (candidate < (distances.get(neighbor) ?? Infinity)) {
        distances.set(neighbor, candidate);
        heap.push([candidate, neighbor]);
      }
    }
  }
  return distances;
}

// Dynamic programming (minimum coins) — O(amount * coins) time
export function coinChange(coins: readonly number[], amount: number): number {
  if (amount < 0 || coins.some((coin) => coin <= 0)) {
    throw new Error("coins must be positive and amount non-negative");
  }
  const dp = Array(amount + 1).fill(amount + 1);
  dp[0] = 0;
  for (let total = 1; total <= amount; total++) {
    for (const coin of coins) {
      if (coin <= total) {
        dp[total] = Math.min(itemAt(dp, total), itemAt(dp, total - coin) + 1);
      }
    }
  }
  return itemAt(dp, amount) > amount ? -1 : itemAt(dp, amount);
}
