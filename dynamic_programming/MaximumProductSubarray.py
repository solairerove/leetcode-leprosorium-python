from typing import List


# O(n) time || O(1) space
def max_product(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    max_so_far, min_so_far = nums[0], nums[0]
    res = max_so_far
    for i in range(1, len(nums)):
        curr = nums[i]
        tmp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
        max_so_far = tmp_max

        res = max(res, max_so_far)

    return res


# O(n) time || O(n) space
def max_product_from_smarter_guy(self, nums: List[int]) -> int:
    reverse = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1
        reverse[i] *= reverse[i - 1] or 1

    return max(nums + reverse)
