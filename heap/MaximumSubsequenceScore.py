import heapq
from typing import List


# O(n * log(n)) time || O(n) space`
def max_score(self, nums1: List[int], nums2: List[int], k: int) -> int:
    total = res = 0
    heap = []
    for a, b in sorted(list(zip(nums1, nums2)), key=lambda ab: -ab[1]):
        heapq.heappush(heap, a)
        total += a

        if len(heap) > k:
            total -= heapq.heappop(heap)

        if len(heap) == k:
            res = max(res, total * b)

    return res
