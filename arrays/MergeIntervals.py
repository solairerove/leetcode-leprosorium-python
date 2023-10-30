from typing import List


# TODO: sorting topic?

# O(n * log(n)) time || O(n) space
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    res = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] > res[-1][1]:
            res.append(intervals[i])
        else:
            res[-1][1] = max(res[-1][1], intervals[i][1])

    return res
