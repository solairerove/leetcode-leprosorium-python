from typing import List


# O(n * log(n)) time || O(1) space
def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True


# O(n * log(n)) time || O(1) space
def can_attend_meetings_short(self, intervals: List[List[int]]) -> bool:
    intervals.sort()
    return all(intervals[i][0] >= intervals[i - 1][1] for i in range(1, len(intervals)))


# O(n * log(n)) time || O(1) space
def can_attend_meetings_short_1(self, intervals: List[List[int]]) -> bool:
    intervals.sort()
    return all(b[0] >= a[1] for a, b in zip(intervals, intervals[1:]))
