import heapq
import random
from collections import Counter
from typing import List


# O(n) time || O(n) space
def top_k_frequent_quickselect(self, nums: List[int], k: int) -> List[int]:
    cnt = Counter(nums)
    unique = list(cnt.keys())

    def partition(low, high, idx):
        freq = cnt[unique[idx]]
        unique[idx], unique[high] = unique[high], unique[idx]

        store_idx = low
        for i in range(low, high):
            if cnt[unique[i]] < freq:
                unique[store_idx], unique[i] = unique[i], unique[store_idx]
                store_idx += 1

        unique[high], unique[store_idx] = unique[store_idx], unique[high]

        return store_idx

    def quick_select(low, high, k_smallest):
        if low == high:
            return

        pivot_idx = random.randint(low, high)
        pivot_idx = partition(low, high, pivot_idx)

        if k_smallest == pivot_idx:
            return
        elif k_smallest < pivot_idx:
            quick_select(low, pivot_idx - 1, k_smallest)
        else:
            quick_select(pivot_idx + 1, high, k_smallest)

    n = len(unique)

    quick_select(0, n - 1, n - k)

    return unique[n - k:]


# O(n * log(k)) time || O(n + k) space
def top_k_frequent_heap(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == k:
        return nums

    cnt = Counter(nums)

    return heapq.nlargest(k, cnt, cnt.get)


# O(n) time || O(n) space
def top_k_frequent_linear(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == k:
        return nums

    cnt = Counter(nums)
    freq = [[] for _ in range(len(nums) + 1)]

    for n, c in cnt.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)

            if len(res) == k:
                return res
