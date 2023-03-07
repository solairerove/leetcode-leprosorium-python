import heapq
from collections import Counter
from typing import List


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
