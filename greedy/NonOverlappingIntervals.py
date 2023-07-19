from typing import List


# O(n * log(n)) time || O(log(n)) space
def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
    end, cnt = float('-inf'), 0
    for s, e in sorted(intervals, key=lambda x: x[1]):
        if s >= end:
            end = e
        else:
            cnt += 1

    return cnt
