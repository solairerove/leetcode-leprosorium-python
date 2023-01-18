# O(n^2) time || O(1) space
def count_substrings(self, s: str) -> int:
    res = 0
    for i in range(len(s)):
        res += count_palindromes(self, s, i, i)
        res += count_palindromes(self, s, i, i + 1)

    return res


def count_palindromes(self, s: str, low: int, high: int) -> int:
    res = 0
    while low >= 0 and high < len(s) and s[low] == s[high]:
        res += 1
        low, high = low - 1, high + 1

    return res
