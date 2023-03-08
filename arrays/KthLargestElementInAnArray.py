import heapq
import random
from typing import List


# O(max(n, n^2) time || O(1) space
def find_kth_largest(self, nums: List[int], k: int) -> int:
    def partition(low, high, pivot_idx):
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]

        store_idx = low
        for i in range(low, high):
            if nums[i] < pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1

        nums[high], nums[store_idx] = nums[store_idx], nums[high]

        return store_idx

    def select(low, high, k_smallest):
        if low == high:
            return nums[low]

        pivot_idx = random.randint(low, high)
        pivot_idx = partition(low, high, pivot_idx)

        if k_smallest == pivot_idx:
            return nums[k_smallest]
        elif k_smallest < pivot_idx:
            return select(low, pivot_idx - 1, k_smallest)
        else:
            return select(pivot_idx + 1, high, k_smallest)

    return select(0, len(nums) - 1, len(nums) - k)


# O(n * log(k)) time || O(k) space
def find_kth_largest_using_heap(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
