import heapq


# O(n) time || O(n) space
class SmallestInfiniteSet:

    def __init__(self):
        self.cnt = 1
        self.heap = []

    def pop_smallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)

        res = self.cnt
        self.cnt += 1

        return res

    def add_back(self, num: int) -> None:
        if num < self.cnt and num not in self.heap:
            heapq.heappush(self.heap, num)
