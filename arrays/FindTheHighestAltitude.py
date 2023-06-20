from itertools import accumulate
from typing import List


# O(n) time || O(n) space
def largest_altitude(self, gain: List[int]) -> int:
    return max(0, max(accumulate(gain)))
