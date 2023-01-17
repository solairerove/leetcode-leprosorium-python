from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    rob1 = rob2 = 0
    for n in nums:
        tmp = max(n + rob1, rob2)
        rob1, rob2 = rob2, tmp

    return rob2


"""
rob1 = rob2 = 0
[1, 2, 3, 1] 4
[1, 2, 3, 1] 4
max(1 + 0, 0), rob1 = 0, rob2 = 1
max(2 + 0, 1), rob1 = 1, rob2 = 2
max(3 + 1, 2), rob1 = 2, rob2 = 4
max(1 + 2, 4), rob1 = 4, rob2 = 4

[2, 7, 9, 3, 1] 12
"""
