import collections
import heapq
from typing import List


class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def add_num(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        self.balance()

    def balance(self):
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self, heap_size):
        if heap_size % 2 == 1:
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2


# O((n - k) + n * log(k)) time || O(n + k) space
def median_sliding_window(self, nums: List[int], k: int) -> List[float]:
    lazy_remove = collections.defaultdict(float)
    median_finder = MedianFinder()
    res = []

    # can be shorter
    for i in range(k):
        median_finder.add_num(nums[i])

    median = median_finder.find_median(k)
    res.append(median)

    for i in range(k, len(nums)):
        head_of_window = nums[i - k]
        lazy_remove[head_of_window] += 1

        balance = -1 if head_of_window <= median else 1

        if nums[i] <= median:
            balance += 1
            heapq.heappush(median_finder.small, -nums[i])
        else:
            balance -= 1
            heapq.heappush(median_finder.large, nums[i])

        if balance < 0:
            heapq.heappush(median_finder.small, -heapq.heappop(median_finder.large))
        elif balance > 0:
            heapq.heappush(median_finder.large, -heapq.heappop(median_finder.small))

        while median_finder.small and lazy_remove[-median_finder.small[0]] > 0:
            lazy_remove[-median_finder.small[0]] -= 1
            heapq.heappop(median_finder.small)

        while median_finder.large and lazy_remove[median_finder.large[0]] > 0:
            lazy_remove[median_finder.large[0]] -= 1
            heapq.heappop(median_finder.large)

        median = median_finder.find_median(k)
        res.append(median)

    return res
