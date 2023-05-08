from typing import List


# O(n ^ 2) time || O(1) space
def diagonal_sum(self, mat: List[List[int]]) -> int:
    res = 0
    n = len(mat)

    for i in range(n):
        for j in range(n):
            if i == j:
                res += mat[i][j]

    for i in range(n):
        for j in range(n):
            if n - i - 1 == n - j - 1:
                res += mat[i][n - j - 1]

    if n % 2 != 0:
        res -= mat[n // 2][n // 2]

    return res
