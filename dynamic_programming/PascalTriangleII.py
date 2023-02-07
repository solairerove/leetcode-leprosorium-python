from typing import List


# O(k^2) time || O(k) space
def get_row(self, row_index: int) -> List[int]:
    row = [1]
    for i in range(row_index):
        for j in range(i, 0, -1):
            row[j] = row[j] + row[j - 1]
        row.append(1)

    return row


def get_row_from_smart_guy(self, row_index: int) -> List[int]:
    row = [1]
    for _ in range(row_index):
        row = [x + y for x, y in zip([0] + row, row + [0])]

    return row
