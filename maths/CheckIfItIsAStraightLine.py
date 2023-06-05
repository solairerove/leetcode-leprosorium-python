from typing import List


# O(n) time || O(1) space
def check_straight_line(self, coordinates: List[List[int]]) -> bool:
    (x0, y0), (x1, y1) = coordinates[: 2]
    for x, y in coordinates:
        if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
            return False

    return True


# O(n) time || O(1) space
def check_straight_line_one_liner(self, coordinates: List[List[int]]) -> bool:
    (x0, y0), (x1, y1) = coordinates[: 2]

    return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)
