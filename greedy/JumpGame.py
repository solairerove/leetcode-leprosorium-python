from typing import List


# O(n) time || O(1) space
def can_jump(self, nums: List[int]) -> bool:
    last_pos = 0
    for i, n in enumerate(nums):
        if i > last_pos:
            return False

        last_pos = max(last_pos, i + n)

    return True
