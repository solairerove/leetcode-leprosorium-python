from typing import List


# O(n * log(a)) time || O(1) space, a - range in nums
def min_cost(self, nums: List[int], cost: List[int]) -> int:
    if min(nums) == max(nums):
        return 0

    def f(x):
        return sum(abs(a - x) * c for a, c in zip(nums, cost))

    low, high = min(nums), max(nums)
    res = f(low)
    while low < high:
        mid = low + (high - low) // 2
        y1, y2 = f(mid), f(mid + 1)
        res = min(y1, y2)

        if y1 < y2:
            high = mid
        else:
            low = mid + 1

    return res
