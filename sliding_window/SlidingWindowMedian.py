import collections
import heapq
from typing import List


class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []
        self.lazy = collections.defaultdict(int)
        self.balance = 0

    def add(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.balance -= 1
        else:
            heapq.heappush(self.large, num)
            self.balance += 1

        self.rebalance()

    def remove(self, num):
        self.lazy[num] += 1
        if num <= -self.small[0]:
            self.balance += 1
        else:
            self.balance -= 1

        self.rebalance()
        self.lazy_remove()

    def find_median(self):
        if self.balance == 0:
            return (-self.small[0] + self.large[0]) / 2
        elif self.balance < 0:
            return -self.small[0]
        else:
            return self.large[0]

    def rebalance(self):
        while self.balance < 0:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.balance += 2

        while self.balance > 0:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.balance -= 2

    def lazy_remove(self):
        while self.small and self.lazy[-self.small[0]] > 0:
            self.lazy[-self.small[0]] -= 1
            heapq.heappop(self.small)

        while self.large and self.lazy[self.large[0]] > 0:
            self.lazy[self.large[0]] -= 1
            heapq.heappop(self.large)


# O(n * log(k)) time || O(n) space
def median_sliding_window(self, nums: List[int], k: int) -> List[float]:
    res = []
    median_finder = MedianFinder()
    for i, num in enumerate(nums):
        median_finder.add(num)

        if i >= k:
            median_finder.remove(nums[i - k])

        if i >= k - 1:
            res.append(median_finder.find_median())

    return res
