from typing import List


# O(n^3) time || O(n^2) space
def min_cost(self, n: int, cuts: List[int]) -> int:
    cuts = sorted(cuts + [0, n])
    k = len(cuts)
    dp = [[0] * k for _ in range(k)]
    for d in range(2, k):
        for i in range(k - d):
            dp[i][i + d] = min(dp[i][m] + dp[m][i + d] for m in range(i + 1, i + d)) + cuts[i + d] - cuts[i]

    return dp[0][k - 1]
