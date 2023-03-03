# O(n * m) time || O(1) space
def str_str(self, haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1

    low, high = 0, 0
    while high < len(haystack):
        i = 0
        while i < len(needle) and high < len(haystack) and haystack[high] == needle[i]:
            if i == len(needle) - 1:
                return low
            high, i = high + 1, i + 1

        if i == 0:
            low += 1 + i
        else:
            low += 1

        high = low

    return -1


# O(n * m) time || O(1) space
def str_str_sliding_window(self, haystack: str, needle: str) -> int:
    m, n = len(needle), len(haystack)
    for window_start in range(n - m + 1):
        for i in range(m):
            if needle[i] != haystack[window_start + i]:
                break
            if i == m - 1:
                return window_start

    return -1
