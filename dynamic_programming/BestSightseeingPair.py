from typing import List


# O(n) time || O(1) space
def max_score_sightseeing_pair(self, values: List[int]) -> int:
    score = max_distance = 0
    for i, e in enumerate(values):
        score = max(score, max_distance + e - i)
        max_distance = max(max_distance, e + i)

    return score
