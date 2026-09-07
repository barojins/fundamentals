from collections import Counter

def frequencies(items):
    return Counter(items)

def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        total = nums[l] + nums[r]
        if total == target:
            return l, r
        if total < target:
            l += 1
        else:
            r -= 1
    return None

def max_window_sum(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("invalid window size")
    window = sum(nums[:k])
    answer = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        answer = max(answer, window)
    return answer

def longest_unique_substring(text):
    last = {}
    left = answer = 0
    for right, char in enumerate(text):
        left = max(left, last.get(char, -1) + 1)
        last[char] = right
        answer = max(answer, right - left + 1)
    return answer

import heapq as hq
import math 

def dijkstra(adj, src):
    inf = math.inf
    dist = {u: math.inf for u in adj}    
    pred = {u: None for u in adj}
    dist[src] = 0

    pq = [(0, src)]
    while pq:
        d, u = hq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u].items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u]+w 
                pred[v] = u 
                hq.heappush(pq, (dist[v], v))
    return dist, pred
        
    

adj = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}
}

def get_path(pred, target):
    path, u = [], target 
    while u is not None:
        path.append(u)
        u = pred[u]
    return path[::-1]

dist, pred = dijkstra(adj, 'A')
print(get_path(pred, 'C'))