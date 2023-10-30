from typing import List


# TODO: is it greedy?

# O(n * log(n)) time || O(log(n)) space
def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])

    end, res = intervals[0][1], 0
    for interval in intervals[1:]:
        if interval[0] >= end:
            end = interval[1]
        else:
            res += 1

    return res
