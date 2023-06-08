from typing import List


# O(m + n) time || O(1) space
def count_negatives(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    r, c, cnt = m - 1, 0, 0
    while r >= 0 and c < n:
        if grid[r][c] < 0:
            cnt, r = cnt + (n - c), r - 1
        else:
            c += 1

    return cnt


# O(m * log(n)) time || O(1) space
def count_negatives_bs(self, grid: List[List[int]]) -> int:
    def bs(row):
        low, high = 0, len(row)
        while low < high:
            mid = low + (high - low) // 2
            if row[mid] < 0:
                high = mid
            else:
                low = mid + 1

        return len(row) - low

    cnt = 0
    for row in grid:
        cnt += bs(row)

    return cnt
