from typing import List


# O(log(m * n)) time || O(1) space
def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    while low <= high:
        mid = low + (high - low) // 2
        num = matrix[mid // cols][mid % cols]

        if target == num:
            return True
        elif target < num:
            high = mid - 1
        else:
            low = mid + 1

    return False
