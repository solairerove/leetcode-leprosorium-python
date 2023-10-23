import functools
from typing import List


# we can use xor here on all elements
# as result we are going to get single number

# O(n) time || O(1) space
def single_number(self, nums: List[int]) -> int:
    res = 0
    for n in nums:
        res ^= n

    return res


# O(n) time || O(1) space
def single_number_reduce(self, nums: List[int]) -> int:
    return functools.reduce(lambda x, y: x ^ y, nums)
