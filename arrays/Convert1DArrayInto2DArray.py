from typing import List


# O(n) time || O(1) space
def construct_2d_array_smart(self, original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != n * m:
        return []

    res = []
    for i in range(0, len(original), n):
        res.append(original[i:i + n])

    return res


# O(n * m) time || O(1) space
def construct_2d_array(self, original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) > m * n:
        return []

    cnt = 0
    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if cnt >= len(original):
                return []

            res[i][j] = original[cnt]
            cnt += 1

    return res
