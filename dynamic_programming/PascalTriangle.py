from operator import add
from typing import List


# O(n^2) time || O(1) space
def generate(self, num_rows: int) -> List[List[int]]:
    triangle = []
    for row_idx in range(num_rows):
        row = [1 for _ in range(row_idx + 1)]

        for i in range(1, len(row) - 1):
            row[i] = triangle[row_idx - 1][i - 1] + triangle[row_idx - 1][i]

        triangle.append(row)

    return triangle


def generate_from_smart_guys(self, num_rows: int) -> List[List[int]]:
    res = [[1]]
    for _ in range(1, num_rows):
        map_ = map(add, [0] + res[-1], res[-1] + [0])
        res.append(list(map_))

    return res if num_rows else []
