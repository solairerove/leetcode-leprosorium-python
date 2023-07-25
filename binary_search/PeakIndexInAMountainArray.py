from typing import List


# O(log(n) time || O(1) space
def peak_index_in_mountain_array(self, arr: List[int]) -> int:
    low, high = 0, len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low
