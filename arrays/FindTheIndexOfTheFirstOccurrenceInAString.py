# O(n) time || O(1) space
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
