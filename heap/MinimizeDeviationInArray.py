import heapq
import math
from typing import List


# O(n * log(n)) time || O(n) space
def minimum_deviation(self, nums: List[int]) -> int:
    res, min_so_far = math.inf, math.inf
    heap = []
    for num in nums:
        curr = -num if num % 2 == 0 else -num * 2
        heapq.heappush(heap, curr)
        min_so_far = min(min_so_far, -curr)

    while heap[0] % 2 == 0:
        res = min(res, -heap[0] - min_so_far)
        min_so_far = min(min_so_far, -heap[0] // 2)
        heapq.heappushpop(heap, heap[0] // 2)

    return min(res, -heap[0] - min_so_far)
