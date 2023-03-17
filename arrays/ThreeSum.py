from typing import List


# O(n^2) time || O(1) space
def three_sum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 3:
        return [nums] if sum(nums) == 0 else []

    res = []
    nums.sort()
    for i, n in enumerate(nums):
        if n > 0:
            break

        if i > 0 and n == nums[i - 1]:
            continue

        low, high = i + 1, len(nums) - 1
        while low < high:
            tree_sum = n + nums[low] + nums[high]

            if tree_sum < 0:
                low += 1
            elif tree_sum > 0:
                high -= 1
            else:
                res.append([n, nums[low], nums[high]])
                low, high = low + 1, high - 1

                while nums[low] == nums[low - 1] and low < high:
                    low += 1

    return res
