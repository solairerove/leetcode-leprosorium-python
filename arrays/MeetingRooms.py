from typing import List


# TODO: sorting topic?

# O(n * log(n)) time || O(1) space
def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


# O(n * log(n)) time || O(1) space
def can_attend_meetings_shorter(self, intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])

    return all(intervals[i][0] >= intervals[i - 1][1] for i in range(1, len(intervals)))
