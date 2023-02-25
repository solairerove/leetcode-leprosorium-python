from typing import List


# O(n * log(sum)) time || O(1) space
def split_array_bs(self, nums: List[int], k: int) -> int:
    low, high = max(nums), sum(nums)
    while low < high:
        mid, total, cnt = low + (high - low) // 2, 0, 1
        for num in nums:
            total, cnt = [(total + num, cnt), (num, cnt + 1)][total + num > mid]
        low, high = [(low, mid), (mid + 1, high)][cnt > k]

    return low
