import collections
from typing import List


# O(n) time || O(n) space
def num_identical_pairs(self, nums: List[int]) -> int:
    cnt, res = collections.defaultdict(int), 0
    for num in nums:
        res, cnt[num] = res + cnt[num], cnt[num] + 1

    return res
