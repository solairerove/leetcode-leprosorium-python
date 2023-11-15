from functools import reduce
from typing import List


# O(n * log(n)) time || O(log(n)) space
def maximum_element_after_decrementing_and_rearranging(self, arr: List[int]) -> int:
    return reduce(lambda res, num: min(res + 1, num), sorted(arr), 0)
