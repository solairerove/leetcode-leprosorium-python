from typing import List


# O(n) time || O(1) space
def max_subarray_sum_circular(self, nums: List[int]) -> int:
    total, max_sum, curr_max, min_sum, curr_min = 0, nums[0], 0, nums[0], 0
    for n in nums:
        curr_max = max(curr_max + n, n)
        max_sum = max(max_sum, curr_max)
        curr_min = min(curr_min + n, n)
        min_sum = min(min_sum, curr_min)
        total += n

    return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
