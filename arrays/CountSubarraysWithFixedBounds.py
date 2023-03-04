from typing import List


# O(n) time || O(1) space
def count_sub_arrays(self, nums: List[int], min_k: int, max_k: int) -> int:
    res = 0
    j_min = j_max = j_bad = -1
    for i, n in enumerate(nums):
        if not min_k <= n <= max_k:
            j_bad = i

        if n == min_k:
            j_min = i

        if n == max_k:
            j_max = i

        res += max(0, min(j_min, j_max) - j_bad)

    return res
