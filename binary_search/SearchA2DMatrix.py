from typing import List


# O(log(m * n)) time || O(1) space
def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    while low <= high:
        mid = low + (high - low) // 2
        mid_row, mid_col = divmod(mid, cols)

        if target == matrix[mid_row][mid_col]:
            return True
        elif target < matrix[mid_row][mid_col]:
            high = mid - 1
        else:
            low = mid + 1

    return False


# O(log(m) + log(n)) time || O(1) space
def search_matrix_2bs(self, matrix: List[List[int]], target: int) -> bool:
    def bs(low, high, row):
        while low <= high:
            mid = low + (high - low) // 2
            if target == matrix[row][mid]:
                return mid
            elif target < matrix[row][mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def bs_row(low, high):
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid]) - 1]:
                return mid
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    row = bs_row(0, len(matrix) - 1)
    if row == -1:
        return False

    col = bs(0, len(matrix[row]) - 1, row)

    return col != -1
