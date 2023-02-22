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


# O(n) time || O(1) space
def find_kth_positive_smart(self, arr: List[int], k: int) -> int:
    kth_missed, i = k, 0
    while i < len(arr) and arr[i] <= kth_missed:
        kth_missed, i = kth_missed + 1, i + 1

    return kth_missed
