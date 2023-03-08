import heapq
from typing import List


# O(n * log(k)) time || O(k) space
def find_kth_largest_using_heap(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
