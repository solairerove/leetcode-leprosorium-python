# O(n^2) time || O(1) space
def longest_palindrome(self, s: str) -> str:
    def expand(i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i, j = i - 1, j + 1

        return s[i + 1: j]

    return max([expand(i, j) for i in range(len(s)) for j in (i, i + 1)], key=len)
