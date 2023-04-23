from typing import List


# O(n * m) time || O(n * m) space
def matrix_block_sum(self, mat: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            dp[r][c] = mat[r - 1][c - 1] + dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1]

    res = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            r1, c1 = max(0, r - k), max(0, c - k)
            r2, c2 = min(m - 1, r + k), min(n - 1, c + k)
            r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
            res[r][c] = dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1 - 1]

    return res
