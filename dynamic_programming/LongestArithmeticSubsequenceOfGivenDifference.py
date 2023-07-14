from typing import List


# O(n) time || O(n) space
def longest_subsequence(self, arr: List[int], difference: int) -> int:
    res = {}
    for num in arr:
        res[num] = res.get(num - difference, 0) + 1

    return max(res.values())
