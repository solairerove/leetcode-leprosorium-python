from typing import List


# O(n + k) time || O(n) space
def sort_array(self, nums: List[int]) -> List[int]:
    counts = {}
    min_val, max_val = min(nums), max(nums)
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    idx = 0
    for num in range(min_val, max_val + 1, 1):
        while counts.get(num, 0) > 0:
            nums[idx] = num
            idx, counts[num] = idx + 1, counts[num] - 1

    return nums
