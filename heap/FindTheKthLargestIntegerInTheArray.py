import heapq
import random
from typing import List


# O(n) time || O(n) space
def kth_largest_number_quickselect(self, nums: List[str], k: int) -> str:
    return str(quickselect([int(num) for num in nums], 0, len(nums) - 1, len(nums) - k))


def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_idx = random.randint(low, high)
    lt, gt = partition(arr, low, high, pivot_idx)
    if k < lt:
        return quickselect(arr, low, lt - 1, k)
    elif k <= gt:
        return arr[k]
    else:
        return quickselect(arr, gt + 1, high, k)


def partition(arr, low, high, pivot_idx):
    pivot = arr[pivot_idx]
    lt, i, gt = low, low, high
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt, i = lt + 1, i + 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1

    return lt, gt


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
