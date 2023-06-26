from heapq import heappush, heappop
from typing import List


# O(k * log(n)) time || O(k * log(n)) space
def total_cost(self, costs: List[int], k: int, candidates: int) -> int:
    heap = []
    low, high = 0, len(costs) - 1

    while low < candidates:
        heappush(heap, (costs[low], low))
        low += 1

    while high >= len(costs) - candidates and high >= low:
        heappush(heap, (costs[high], high))
        high -= 1

    res = 0
    for i in range(k):
        c, idx = heappop(heap)
        res += c

        if idx < low:
            if low <= high:
                heappush(heap, (costs[low], low))
                low += 1
        else:
            if low <= high:
                heappush(heap, (costs[high], high))
                high -= 1

    return res
