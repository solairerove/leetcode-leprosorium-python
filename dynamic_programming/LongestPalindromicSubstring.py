# O(n^2) time || O(1) space
def longest_palindrome(self, s: str) -> str:
    res = ""
    for i in range(len(s)):
        res = get_palindrome_from(self, s, res, i, i)
        res = get_palindrome_from(self, s, res, i, i + 1)

    return res


def get_palindrome_from(self, s: str, res: str, low: int, high: int) -> str:
    while low >= 0 and high < len(s) and s[low] == s[high]:
        if high - low + 1 > len(res):
            res = s[low: high + 1]
        low, high = low - 1, high + 1

    return res
