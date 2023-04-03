from typing import List


# O(n) time || O(1) space
def min_operations(self, nums1: List[int], nums2: List[int]) -> int:
    if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
        return -1

    sum1, sum2 = sum(nums1), sum(nums2)
    if sum1 > sum2:
        return min_operations(self, nums2, nums1)

    cnt = [0] * 6
    for n in nums1:
        cnt[6 - n] += 1  # count increases

    for n in nums2:
        cnt[n - 1] += 1  # count decreases

    i, res = 5, 0
    while sum2 > sum1:
        while cnt[i] == 0:
            i -= 1

        sum1 += i
        cnt[i], res = cnt[i] - 1, res + 1

    return res
