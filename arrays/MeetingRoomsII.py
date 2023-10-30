from typing import List


# TODO: sorting topic?

# O(n * log(n)) time || O(n) space
def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    res = 0
    start, end = 0, 0
    while start < len(intervals):
        if start_times[start] >= end_times[end]:
            res, end = res - 1, end + 1

        res, start = res + 1, start + 1

    return res
