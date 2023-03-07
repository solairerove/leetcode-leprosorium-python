import heapq
from collections import Counter
from typing import List


# O(n * log(k)) time || O(n + k) space
def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == k:
        return nums

    cnt = Counter(nums)

    return heapq.nlargest(k, cnt, cnt.get)
