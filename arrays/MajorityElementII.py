from typing import List


# O(n) time || O(1) space
def majority_element(self, nums: List[int]) -> List[int]:
    if not nums:
        return []

    cnt1, cnt2, can1, can2 = 0, 0, None, None
    for n in nums:
        if can1 == n:
            cnt1 += 1
        elif can2 == n:
            cnt2 += 1
        elif cnt1 == 0:
            can1, cnt1 = n, cnt1 + 1
        elif cnt2 == 0:
            can2, cnt2 = n, cnt2 + 1
        else:
            cnt1, cnt2 = cnt1 - 1, cnt2 - 1

    res = []
    for c in [can1, can2]:
        if nums.count(c) > len(nums) // 3:
            res.append(c)

    return res
