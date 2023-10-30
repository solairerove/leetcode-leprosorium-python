from typing import List


# TODO: sorting topic?

# O(n * log(n)) time || O(1) space
def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    res = 0
    low, high = 0, 0
    while low < len(intervals):
        if start_times[low] >= end_times[high]:
            res, high = res - 1, high + 1

        res, low = res + 1, low + 1

    return res
