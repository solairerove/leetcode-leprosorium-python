# O(n^2) time || O(1) space
def count_substrings(self, s: str) -> int:
    def count_palindromes(low: int, high: int) -> int:
        res = 0
        while low >= 0 and high < len(s) and s[low] == s[high]:
            res += 1
            low, high = low - 1, high + 1

        return res

    count = 0
    for i in range(len(s)):
        count += count_palindromes(i, i)
        count += count_palindromes(i, i + 1)

    return count
