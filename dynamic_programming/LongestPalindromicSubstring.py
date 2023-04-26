# O(n^2) time || O(1) space
def longest_palindrome(self, s: str) -> str:
    if s == s[::-1]:
        return s

    def get_palindrome_from(i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i, j = i - 1, j + 1

        return s[i + 1: j]

    res = s[0]
    for i in range(1, len(s)):
        res = max([res, get_palindrome_from(i - 1, i), get_palindrome_from(i - 1, i + 1)], key=len)

    return res
