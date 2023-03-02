from typing import List


# O(n) time || O(n) space
def two_sum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        to_find = target - nums[i]
        if to_find in dic:
            return [dic[to_find], i]
        else:
            dic[nums[i]] = i

    return []
