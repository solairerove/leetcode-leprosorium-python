import math
from typing import List


# O(n * log(m)) time || O(n) space, where m is diff between [-1] and [0]
def minmax_gas_dist(self, stations: List[int], k: int) -> float:
    low, high = 1e-6, stations[-1] - stations[0]
    while low + 1e-6 < high:
        mid = (low + high) / 2
        cnt = 0
        for a, b in zip(stations, stations[1:]):
            cnt += math.ceil((b - a) / mid) - 1

        if cnt > k:
            low = mid
        else:
            high = mid

    return high
