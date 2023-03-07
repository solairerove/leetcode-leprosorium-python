from typing import List


# O(n * log(m * k) time || O(1) space
# n - length of time
# m - total limit of total_trips
# k - max time taken by one trip
def minimum_time(self, time: List[int], total_trips: int) -> int:
    low, high = 1, min(time) * total_trips

    def enough_time(given_time):
        return sum(given_time // t for t in time) >= total_trips

    while low < high:
        mid = low + (high - low) // 2
        if not enough_time(mid):
            low = mid + 1
        else:
            high = mid

    return low
