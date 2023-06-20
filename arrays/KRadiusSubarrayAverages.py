from typing import List


# O(n) time || O(1) space
def get_averages(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = [-1] * n

    left, curr_window_sum, diameter = 0, 0, 2 * k + 1
    for right in range(n):
        curr_window_sum += nums[right]
        if right - left + 1 >= diameter:
            res[left + k] = curr_window_sum // diameter
            curr_window_sum -= nums[left]
            left += 1

    return res
