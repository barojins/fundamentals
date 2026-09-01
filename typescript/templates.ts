/** Compact coding-interview templates. */

// Frequency map — O(n) time, O(n) space
export function frequencies<T>(items: T[]): Map<T, number> {
  const counts = new Map<T, number>();
  for (const item of items) counts.set(item, (counts.get(item) ?? 0) + 1);
  return counts;
}

// Two pointers (sorted input) — O(n) time, O(1) space
export function twoSumSorted(nums: number[], target: number): [number, number] | null {
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    const total = nums[left] + nums[right];
    if (total === target) return [left, right];
    total < target ? left++ : right--;
  }
  return null;
}

// Fixed sliding window — O(n) time, O(1) space
export function maxWindowSum(nums: number[], k: number): number {
  if (k <= 0 || k > nums.length) throw new Error("k must be between 1 and nums.length");
  let window = nums.slice(0, k).reduce((sum, num) => sum + num, 0);
  let best = window;
  for (let right = k; right < nums.length; right++) {
    window += nums[right] - nums[right - k];
    best = Math.max(best, window);
  }
  return best;
}

// Variable sliding window — O(n) time, O(n) space
export function longestUniqueSubstring(text: string): number {
  const lastSeen = new Map<string, number>();
  let left = 0;
  let best = 0;
  for (let right = 0; right < text.length; right++) {
    left = Math.max(left, (lastSeen.get(text[right]) ?? -1) + 1);
    lastSeen.set(text[right], right);
    best = Math.max(best, right - left + 1);
  }
  return best;
}

// Prefix sum — build O(n), range query O(1)
export function prefixSums(nums: number[]): number[] {
  const prefix = [0];
  for (const num of nums) prefix.push(prefix[prefix.length - 1] + num);
  return prefix;
}

export function rangeSum(prefix: number[], left: number, right: number): number {
  return prefix[right + 1] - prefix[left];
}

// Kadane's algorithm — O(n) time, O(1) space
export function maxSubarray(nums: number[]): number {
  if (nums.length === 0) throw new Error("nums must not be empty");
  let current = nums[0];
  let best = nums[0];
  for (const num of nums.slice(1)) {
    current = Math.max(num, current + num);
    best = Math.max(best, current);
  }
  return best;
}

// Binary search — O(log n) time, O(1) space
export function binarySearch(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;
  while (left <= right) {
    const middle = Math.floor((left + right) / 2);
    if (nums[middle] === target) return middle;
    if (nums[middle] < target) left = middle + 1;
    else right = middle - 1;
  }
  return -1;
}

export class ListNode {
  constructor(public value: number, public next: ListNode | null = null) {}
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
    slow = slow!.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}

// Monotonic stack (next greater value) — O(n) time, O(n) space
export function nextGreater(nums: number[]): number[] {
  const answer = Array(nums.length).fill(-1);
  const stack: number[] = [];
  nums.forEach((num, index) => {
    while (stack.length && nums[stack[stack.length - 1]] < num) {
      answer[stack.pop()!] = num;
    }
    stack.push(index);
  });
  return answer;
}

export type Graph<T> = Map<T, T[]>;

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

// Iterative DFS — O(V + E) time, O(V) space
export function dfsIterative<T>(graph: Graph<T>, start: T): T[] {
  const order: T[] = [];
  const seen = new Set<T>();
  const stack = [start];
  while (stack.length) {
    const node = stack.pop()!;
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
    const node = queue[front];
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
export function subsets(nums: number[]): number[][] {
  const answer: number[][] = [];
  const path: number[] = [];
  const backtrack = (index: number): void => {
    if (index === nums.length) {
      answer.push([...path]);
      return;
    }
    backtrack(index + 1);
    path.push(nums[index]);
    backtrack(index + 1);
    path.pop();
  };
  backtrack(0);
  return answer;
}

class MinHeap<T> {
  private data: T[] = [];
  constructor(private less: (a: T, b: T) => boolean) {}

  get size(): number { return this.data.length; }

  push(value: T): void {
    this.data.push(value);
    for (let child = this.data.length - 1; child > 0;) {
      const parent = Math.floor((child - 1) / 2);
      if (!this.less(this.data[child], this.data[parent])) break;
      [this.data[child], this.data[parent]] = [this.data[parent], this.data[child]];
      child = parent;
    }
  }

  pop(): T | undefined {
    if (!this.data.length) return undefined;
    const root = this.data[0];
    const last = this.data.pop()!;
    if (this.data.length) {
      this.data[0] = last;
      for (let parent = 0;;) {
        let child = parent * 2 + 1;
        if (child >= this.data.length) break;
        if (child + 1 < this.data.length && this.less(this.data[child + 1], this.data[child])) child++;
        if (!this.less(this.data[child], this.data[parent])) break;
        [this.data[child], this.data[parent]] = [this.data[parent], this.data[child]];
        parent = child;
      }
    }
    return root;
  }

  peek(): T | undefined { return this.data[0]; }
}

// Heap / top K — O(n log k) time, O(k) space
export function topK(nums: number[], k: number): number[] {
  const heap = new MinHeap<number>((a, b) => a < b);
  for (const num of nums) {
    heap.push(num);
    if (heap.size > k) heap.pop();
  }
  const answer: number[] = [];
  while (heap.size) answer.push(heap.pop()!);
  return answer.reverse();
}

// Merge intervals — O(n log n) time, O(n) space
export function mergeIntervals(intervals: number[][]): number[][] {
  const merged: number[][] = [];
  for (const [start, end] of [...intervals].sort((a, b) => a[0] - b[0])) {
    if (!merged.length || start > merged[merged.length - 1][1]) merged.push([start, end]);
    else merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], end);
  }
  return merged;
}

// Dijkstra (non-negative weights) — O((V + E) log V) time
export type WeightedGraph = Map<string, Array<[string, number]>>;

export function dijkstra(graph: WeightedGraph, start: string): Map<string, number> {
  const distances = new Map<string, number>([[start, 0]]);
  const heap = new MinHeap<[number, string]>((a, b) => a[0] < b[0]);
  heap.push([0, start]);
  while (heap.size) {
    const [distance, node] = heap.pop()!;
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
export function coinChange(coins: number[], amount: number): number {
  const dp = Array(amount + 1).fill(amount + 1);
  dp[0] = 0;
  for (let total = 1; total <= amount; total++) {
    for (const coin of coins) {
      if (coin <= total) dp[total] = Math.min(dp[total], dp[total - coin] + 1);
    }
  }
  return dp[amount] > amount ? -1 : dp[amount];
}
