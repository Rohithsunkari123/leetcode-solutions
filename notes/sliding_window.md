# 🪟 Sliding Window — Concept Notes

## Core Idea
Reduce nested O(n²) loops to a single O(n) pass by maintaining a "window"
(a contiguous subarray/substring) that slides across the input.

---

## Template 1: Fixed Window (size = k)

```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    result = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # slide: add right, remove left
        result = max(result, window_sum)

    return result
```

---

## Template 2: Variable Window

```python
def variable_window(arr):
    left = 0
    result = 0

    for right in range(len(arr)):
        # 1. Expand — include arr[right] in window

        while window_is_invalid():
            # 2. Shrink — remove arr[left] from window
            left += 1

        # 3. Window is valid — update result
        result = max(result, right - left + 1)

    return result
```

---

## Pattern: "Exactly K" → atMost(K) - atMost(K-1)

When asked "count subarrays with exactly K distinct/odd/etc.":

```python
def exactly_k(arr, k):
    return at_most(arr, k) - at_most(arr, k - 1)

def at_most(arr, k):
    left = 0
    count = 0
    # ... variable window counting subarrays with at most k of something
    return count
```

---

## Pattern: Fixed Window + Monotonic Deque (for max/min)

```python
from collections import deque

def sliding_window_max(nums, k):
    dq = deque()   # stores indices, decreasing order of values
    result = []

    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)

        if dq[0] == i - k:      # left edge out of window
            dq.popleft()

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

---

## Problem → Pattern Cheatsheet

| Problem Type | Pattern |
|---|---|
| Max/min sum of window of size k | Fixed Window |
| Longest subarray satisfying condition | Variable Window — maximize length |
| Shortest subarray satisfying condition | Variable Window — minimize length |
| Count subarrays with exactly K | atMost(K) - atMost(K-1) |
| Max element in every window | Monotonic Deque |
| Window involves character frequencies | HashMap / array[26] |

---

## Solved Problems

| # | Problem | Difficulty |
|---|---------|------------|
| 3 | Longest Substring Without Repeating Characters | 🟡 Medium |
