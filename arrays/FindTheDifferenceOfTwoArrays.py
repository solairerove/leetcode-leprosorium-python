from typing import List


# O(n) time || O(n) space
def find_difference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    s1, s2 = set(nums1), set(nums2)

    return [list(s1 - s2), list(s2 - s1)]


# O(m + n) time || O(m + n) space
def find_difference_naive(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1, set2 = set(nums1), set(nums2)
    distinct1, distinct2 = set(), set()

    for num in nums2:
        if num not in set1:
            distinct2.add(num)

    for num in nums1:
        if num not in set2:
            distinct1.add(num)

    return [list(distinct1), list(distinct2)]
