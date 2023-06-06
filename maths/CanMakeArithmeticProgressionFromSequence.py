from typing import List


# O(n * log(n)) time || O(1) space
def can_make_arithmetic_progression_sorting(self, arr: List[int]) -> bool:
    arr.sort()

    return all(arr[i - 2] - arr[i - 1] == arr[i - 1] - arr[i] for i in range(2, len(arr)))
