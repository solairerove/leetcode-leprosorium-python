from functools import lru_cache


# O(n * log(k)) time || O(n) space
def number_of_arrays_top_down(self, s: str, k: int) -> int:
    @lru_cache(None)
    def dp(i):
        if i == len(s):
            return 1

        if s[i] == "0":
            return 0

        res, curr = 0, ''
        for j in range(i, len(s)):
            curr += s[j]
            if int(curr) > k:
                break

            res += dp(j + 1)

        return res % (10 ** 9 + 7)

    return dp(0)
