from bisect import bisect_left
from typing import List


# O(n * log(n) + m * log(m)) time || O(n) space
def successful_pairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()

    return [len(potions) - bisect_left(potions, (success + s - 1) // s) for s in spells]
