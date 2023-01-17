# O(n^2) time || O(1) space
def longest_palindrome(self, s: str) -> str:
    res = ""
    for i in range(len(s)):
        low = high = i
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > len(res):
                res = s[low: high + 1]
            low, high = low - 1, high + 1

        low, high = i, i + 1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > len(res):
                res = s[low: high + 1]
            low, high = low - 1, high + 1

    return res
