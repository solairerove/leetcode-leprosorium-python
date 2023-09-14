from typing import List


# O(n) time || O(n) space
def two_sum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        to_find = target - num
        if to_find in dic:
            return [dic[to_find], i]

        dic[num] = i

    return [-1, -1]
