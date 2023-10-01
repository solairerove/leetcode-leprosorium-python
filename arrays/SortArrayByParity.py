from typing import List


# O(n) time || O(1) space
def sort_array_by_parity(self, nums: List[int]) -> List[int]:
    low, high = 0, len(nums) - 1
    while low < high:
        # odd -> even swap
        if nums[low] % 2 > nums[high] % 2:
            nums[low], nums[high] = nums[high], nums[low]

        if nums[low] % 2 == 0:
            low += 1

        if nums[high] % 2 == 1:
            high -= 1

    return nums


# O(n) time || O(n) space
def sort_array_by_parity_two_pass(self, nums: List[int]) -> List[int]:
    return (
            [x for x in nums if x % 2 == 0] +
            [x for x in nums if x % 2 == 1]
    )


# O(n * log(n)) time || O(n) space
def sort_array_by_parity_sort(self, nums: List[int]) -> List[int]:
    nums.sort(key=lambda x: x % 2)

    return nums
