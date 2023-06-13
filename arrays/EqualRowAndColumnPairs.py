import collections
from typing import List


# O(n^2) time || O(n^2) space
def equal_pairs(self, grid: List[List[int]]) -> int:
    freq = collections.Counter(tuple(row) for row in grid)

    return sum(freq[tuple(col)] for col in zip(*grid))
