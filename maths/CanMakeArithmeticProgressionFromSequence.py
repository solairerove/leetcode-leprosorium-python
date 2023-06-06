from typing import List


# O(n) time || O(n) space
def can_make_arithmetic_progression(self, arr: List[int]) -> bool:
    mi, mx, n, s = min(arr), max(arr), len(arr), set(arr)
    if (mx - mi) % (n - 1) != 0:
        return False

    diff = (mx - mi) // (n - 1)
    for _ in range(n):
        if mi not in s:
            return False

        mi += diff

    return True


# O(n * log(n)) time || O(1) space
def can_make_arithmetic_progression_sorting(self, arr: List[int]) -> bool:
    arr.sort()

    return all(arr[i - 2] - arr[i - 1] == arr[i - 1] - arr[i] for i in range(2, len(arr)))
