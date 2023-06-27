import heapq
from typing import List


# O(k * log(k)) time || O(k) space
def k_smallest_pairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    heap = []

    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(heap, [nums1[i] + nums2[j], i, j])

    push(0, 0)
    res = []
    while heap and len(res) < k:
        _, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)

    return res
