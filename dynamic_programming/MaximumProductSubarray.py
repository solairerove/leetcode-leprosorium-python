from typing import List


# O(n) time || O(1) space
def max_product(self, nums: List[int]) -> int:
    res = nums[0]
    curr_min = curr_max = 1
    for n in nums:
        tmp_max = curr_max * n
        curr_max = max(curr_max * n, curr_min * n, n)
        curr_min = min(tmp_max, curr_min * n, n)
        res = max(res, curr_max)

    return res


# O(n) time || O(1) space
def max_product_from_smarter_guy(self, nums: List[int]) -> int:
    reverse = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        reverse[i] *= reverse[i - 1] or 1

    return max(nums + reverse)
