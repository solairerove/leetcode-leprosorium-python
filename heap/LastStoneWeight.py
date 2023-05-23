import heapq
from typing import List


# O(n * log(n)) time || O(n) space
def last_stone_weight(self, stones: List[int]) -> int:
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1 and heap[0] != 0:
        stone = heapq.heappop(heap) - heapq.heappop(heap)
        heapq.heappush(heap, stone)

    return -heap[0]
