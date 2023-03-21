from typing import List


# O(n) time || O(1) space
def zero_filled_subarray(self, nums: List[int]) -> int:
    res = num_subarray = 0
    for num in nums:
        if num == 0:
            num_subarray += 1
        else:
            num_subarray = 0
        res += num_subarray

    return res
