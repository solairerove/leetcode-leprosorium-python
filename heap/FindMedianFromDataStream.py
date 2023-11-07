from heapq import heappush, heappop


class MedianFinder:

    # O(1) time || O(n) space
    def __init__(self):
        self.small = []  # [0] is highest among small numbers, max heap
        self.large = []  # [0] is lowest among large numbers, min heap

    # O(log(n)) time || O(n) space
    def add_num(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))

        if len(self.small) < len(self.large):
            heappush(self.small, -heappop(self.large))

    # O(1) time || O(1) space
    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2
