from typing import List


# O(n * log(n)) time || O(log(n)) space
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # merged[-1][1] = interval[1]
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
