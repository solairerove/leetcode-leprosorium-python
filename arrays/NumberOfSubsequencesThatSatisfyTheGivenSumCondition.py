from typing import List


# O(n * log(n)) time || O(1) space
def num_subseq(self, nums: List[int], target: int) -> int:
    nums.sort()
    low, high = 0, len(nums) - 1
    res = 0
    mod = 10 ** 9 + 7
    while low <= high:
        if nums[low] + nums[high] > target:
            high -= 1
        else:
            res += pow(2, high - low, mod)
            low += 1

    return res % mod
