# O(n^2) time || O(1) space
def longest_palindrome(self, s: str) -> str:
    def get_palindrome_from(low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low, high = low - 1, high + 1

        return s[low + 1: high]

    return max([get_palindrome_from(i, j) for i in range(len(s)) for j in (i, i + 1)], key=len)
