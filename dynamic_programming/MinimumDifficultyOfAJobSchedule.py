from functools import lru_cache
from typing import List


# O(d * ((n - d) ^ 2)) time || O(d * (n - d)) space
def min_difficulty_top_down(self, job_difficulty: List[int], d: int) -> int:
    n = len(job_difficulty)

    if n < d:
        return -1

    hardest_job_remaining = [0] * n
    hardest_job = 0
    for i in range(n - 1, -1, -1):
        hardest_job = max(hardest_job, job_difficulty[i])
        hardest_job_remaining[i] = hardest_job

    @lru_cache(None)
    def dp(i: int, day: int) -> int:
        if day == d:
            return hardest_job_remaining[i]

        best = float("inf")
        hardest = 0
        for j in range(i, n - (d - day)):
            hardest = max(hardest, job_difficulty[j])
            best = min(best, hardest + dp(j + 1, day + 1))

        return best

    return dp(0, 1)


# O(d * ((n - d) ^ 2)) time || O(d * n) space
def min_difficulty_bottom_up(self, job_difficulty: List[int], d: int) -> int:
    n = len(job_difficulty)

    if n < d:
        return -1

    dp = [[float("inf")] * (d + 1) for _ in range(n)]
    dp[-1][d] = job_difficulty[-1]

    for i in range(n - 2, -1, -1):
        dp[i][d] = max(dp[i + 1][d], job_difficulty[i])

    for day in range(d - 1, 0, -1):
        for i in range(day - 1, n - (d - day)):
            hardest = 0
            for j in range(i, n - (d - day)):
                hardest = max(hardest, job_difficulty[j])
                dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])

    return int(dp[0][1])
