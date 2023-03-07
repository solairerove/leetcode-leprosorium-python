from typing import List


# O(n * log(m * k) time || O(1) space
# n - length of time
# m - total limit of total_trips
# k - max time taken by one trip
def minimum_time(self, time: List[int], total_trips: int) -> int:
    low, high = 1, max(time) * total_trips

    def enough_time(given_time):
        actual_trips = 0
        for t in time:
            actual_trips += given_time // t

        return actual_trips >= total_trips

    while low < high:
        mid = low + (high - low) // 2
        if enough_time(mid):
            high = mid
        else:
            low = mid + 1

    return low
