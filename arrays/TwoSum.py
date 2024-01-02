import collections
from typing import List


# O(n) time || O(n) space
def two_sum(self, nums: List[int], target: int) -> List[int]:
    dic = collections.defaultdict(int)
    for i, num in enumerate(nums):
        if target - num in dic:
            return [i, dic[target - num]]

        dic[num] = i
