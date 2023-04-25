from typing import List


# O(n * m) time || O(n * m) space
def maximal_square(self, matrix: List[List[str]]) -> int:
    if not matrix or len(matrix) < 1:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_so_far = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                max_so_far = max(max_so_far, dp[i + 1][j + 1])

    return max_so_far * max_so_far
