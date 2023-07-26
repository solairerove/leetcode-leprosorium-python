from typing import List


# O(n * log(k)) time || O(1) space
def min_speed_on_time(self, dist: List[int], hour: float) -> int:
    low, high, n = 1, 10 ** 7 + 1, len(dist)
    while low < high:
        speed = low + (high - low) // 2
        need = dist[-1] / speed + sum((dist[i] + speed - 1) // speed for i in range(n - 1))

        if need > hour:
            low = speed + 1
        else:
            high = speed

    return -1 if low == 10 ** 7 + 1 else low
