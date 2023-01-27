from typing import List


# O(n) time || O(1) space
def find_duplicates(self, nums: List[int]) -> List[int]:
    res = []
    for n in nums:
        if nums[abs(n) - 1] < 0:
            res.append(abs(n))
        else:
            nums[abs(n) - 1] *= -1

    return res
