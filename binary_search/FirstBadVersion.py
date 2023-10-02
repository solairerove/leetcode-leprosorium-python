# O(log(n)) time || O(1) space
def first_bad_version(self, n: int, bad_version: int) -> int:
    low, high = 1, n
    while low <= high:
        mid = low + (high - low) // 2
        if is_bad_version(self, mid, bad_version):
            high = mid - 1
        else:
            low = mid + 1

    return low


def is_bad_version(self, version: int, bad_version: int) -> bool:
    return version >= bad_version
