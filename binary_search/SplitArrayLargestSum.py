from typing import List


# O(n * log(n)) time || O(n) space
def split_array_top_down(self, nums: List[int], k: int) -> int:
    return -1


# O(n * log(sum)) time || O(1) space
def split_array_bs(self, nums: List[int], k: int) -> int:
    low, high = max(nums), sum(nums)
    while low < high:
        mid, curr_sum, cnt = low + (high - low) // 2, 0, 1
        for num in nums:
            curr_sum, cnt = [(curr_sum + num, cnt), (num, cnt + 1)][curr_sum + num > mid]
        low, high = [(low, mid), (mid + 1, high)][cnt > k]

    return low
