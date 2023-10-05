from typing import List


# O(n) time || O(1) space
def majority_element(self, nums: List[int]) -> int:
    cnt, can = 0, None
    for num in nums:
        if can == num:
            cnt += 1
        elif cnt == 0:
            can = num
        else:
            cnt -= 1

    return can
