from functools import lru_cache


# O(n^2) time || O(n^2) space
def longest_palindrome_subseq_top_down(self, s: str) -> int:
    @lru_cache(None)
    def dp(low, high):
        if low > high:
            return 0

        if low == high:
            return 1

        if s[low] == s[high]:
            return dp(low + 1, high - 1) + 2

        return max(dp(low, high - 1), dp(low + 1, high))

    return dp(0, len(s) - 1)
