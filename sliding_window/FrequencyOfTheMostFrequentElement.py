from typing import List


# O(n * log(n)) time | O(log(n)) space
def max_frequency(self, nums: List[int], k: int) -> int:
    nums.sort()
    low, res, total = 0, 0, 0
    for high in range(len(nums)):
        total += nums[high]

        while nums[high] * (high - low + 1) - total > k:
            total -= nums[low]
            low += 1

        res = max(res, high - low + 1)

    return res
