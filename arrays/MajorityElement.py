from collections import Counter
from typing import List


# O(n) time || O(n) space
def majority_element_hm(self, nums: List[int]) -> int:
    cnt = Counter(nums)

    return max(cnt.keys(), key=cnt.get)
