from typing import List


# O(n * m) time || O(n * m) space
def maximal_square(self, matrix: List[List[str]]) -> int:
    if not matrix or len(matrix) < 1:
        return 0

    rows, columns = len(matrix), len(matrix[0])

    dp = [[0] * (columns + 1) for _ in range(rows + 1)]
    max_so_far = 0

    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == '1':
                dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1
                max_so_far = max(max_so_far, dp[r + 1][c + 1])

    return max_so_far * max_so_far
