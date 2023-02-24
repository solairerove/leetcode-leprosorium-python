from typing import List


# O(n) time || O(n) space
def two_sum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i, n in enumerate(nums):
        actual = target - n
        if actual in dic:
            return [dic[actual], i]
        else:
            dic[n] = i

    return []
