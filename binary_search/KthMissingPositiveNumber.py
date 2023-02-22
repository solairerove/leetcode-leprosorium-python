from typing import List


# O(log(n)) time || O(1) space
def find_kth_positive(self, arr: List[int], k: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] - mid - 1 < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k
