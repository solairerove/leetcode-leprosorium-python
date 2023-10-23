import math
from typing import List


# O(n * log(max(p)) time || O(1) space
def min_eating_speed(self, piles: List[int], h: int) -> int:
    low, high = 1, max(piles)
    while low < high:
        hours, mid = 0, low + (high - low) // 2
        if sum((math.ceil(pile / mid)) for pile in piles) <= h:
            high = mid
        else:
            low = mid + 1

    return high
