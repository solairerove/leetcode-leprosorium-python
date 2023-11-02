import heapq
from typing import List


# O(n * log(k * m)) time || O(k) space
# n is len of nums
# m is len of each num
# k is k
def kth_largest_number_heap(self, nums: List[str], k: int) -> str:
    heap = []
    for num in nums:
        heapq.heappush(heap, int(num))
        if len(heap) > k:
            heapq.heappop(heap)

    return str(heap[0])
