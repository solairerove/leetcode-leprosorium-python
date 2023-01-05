from collections import defaultdict
from random import choice


class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.map = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.map[val].add(len(self.list))
        self.list.append(val)

        return len(self.map[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.map[val]:
            return False

        remove_idx, last = self.map[val].pop(), self.list[-1]
        self.list[remove_idx] = last
        self.map[last].add(remove_idx)
        self.map[last].discard(len(self.list) - 1)
        self.list.pop()

        return True

    def get_random(self) -> int:
        return choice(self.list)
