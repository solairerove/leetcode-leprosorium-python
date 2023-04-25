# O(n) time || O(n) space
class SmallestInfiniteSet:

    def __init__(self):
        self.cnt = 1
        self.added = set()

    def pop_smallest(self) -> int:
        if len(self.added) != 0:
            res = min(self.added)
            self.added.remove(res)

            return res

        res = self.cnt
        self.cnt += 1

        return res

    def add_back(self, num: int) -> None:
        if num < self.cnt:
            self.added.add(num)
