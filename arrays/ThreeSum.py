from typing import List


# O(n^2) time || O(1) space
def three_sum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        low, high = i + 1, len(nums) - 1
        while low < high:
            _sum = nums[i] + nums[low] + nums[high]
            if _sum == 0:
                res.append([nums[i], nums[low], nums[high]])
                low, high = low + 1, high - 1

                while low < high and nums[low] == nums[low - 1]:
                    low += 1

                while low < high and nums[high] == nums[high + 1]:
                    high -= 1

            elif _sum < 0:
                low += 1
            else:
                high -= 1

    return res
