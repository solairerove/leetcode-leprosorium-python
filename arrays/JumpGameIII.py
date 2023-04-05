from typing import List


# O(n) time || O(n) space,
def can_reach(self, arr: List[int], start: int) -> bool:
    if 0 <= start < len(arr) and arr[start] >= 0:
        arr[start] = -arr[start]

        return arr[start] == 0 or can_reach(self, arr, arr[start] + start) or can_reach(self, arr, start - arr[start])

    return False
