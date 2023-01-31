from typing import List


# O(n) time || O(1) space
def rob(self, nums: List[int]) -> int:
    rob1 = rob2 = 0
    for n in nums:
        rob1, rob2 = rob2, max(n + rob1, rob2)

    return rob2
