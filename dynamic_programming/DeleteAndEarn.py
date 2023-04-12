import collections
from collections import Counter
from functools import cache
from typing import List


# O(max(n)) time || O(max(n)) space
def delete_and_earn(self, nums: List[int]) -> int:
    points, prev, curr = Counter(nums), 0, 0

    for value in range(min(points.keys()), max(points.keys()) + 1):
        prev, curr = curr, max(prev + value * points[value], curr)

    return curr


# O(n + k) time || O(n + k) space
def delete_and_earn_top_down(self, nums: List[int]) -> int:
    points = collections.defaultdict(int)
    max_number = 0
    for num in nums:
        points[num] += num
        max_number = max(max_number, num)

    @cache
    def dp(i):
        if i == 0:
            return 0

        if i == 1:
            return points[1]

        return max(dp(i - 1), dp(i - 2) + points[i])

    return dp(max_number)
