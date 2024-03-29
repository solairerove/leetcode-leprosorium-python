from typing import List


# O(n^3) time || O(1) space
def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            low, high = j + 1, len(nums) - 1
            while low < high:
                _sum = nums[i] + nums[j] + nums[low] + nums[high]

                if _sum == target:
                    res.append([nums[i], nums[j], nums[low], nums[high]])
                    low, high = low + 1, high - 1

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif _sum < target:
                    low += 1
                else:
                    high -= 1

    return res
