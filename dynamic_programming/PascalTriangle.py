from operator import add
from typing import List


def generate_from_smart_guys(self, num_rows: int) -> List[List[int]]:
    res = [[1]]
    for _ in range(1, num_rows):
        map_ = map(add, [0] + res[-1], res[-1] + [0])
        res.append(list(map_))

    return res if num_rows else []
