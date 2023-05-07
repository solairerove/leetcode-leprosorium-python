import bisect
from typing import List


# O(n * log(n)) time || O(n) space
def longest_obstacle_course_at_each_position(self, obstacles: List[int]) -> List[int]:
    mono, res = [], []
    for o in obstacles:
        i = bisect.bisect(mono, o)
        res.append(i + 1)
        if i == len(mono):
            mono.append(0)

        mono[i] = o

    return res
