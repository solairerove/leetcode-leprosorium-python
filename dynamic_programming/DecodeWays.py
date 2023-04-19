from functools import lru_cache


# O(n) time || O(1) space
def num_decodings(self, s: str) -> int:
    if s[0] == "0":
        return 0

    one_back = two_back = 1
    for i in range(1, len(s)):
        curr = 0
        if s[i] != "0":
            curr = one_back

        two_digits = int(s[i - 1: i + 1])
        if 9 < two_digits < 27:
            curr += two_back
        two_back, one_back = one_back, curr

    return one_back


# O(n) time || O(n) space
def num_decodings_top_down(self, s: str) -> int:
    @lru_cache(None)
    def dp(i):
        if i == len(s):
            return 1

        if s[i] == "0":
            return 0

        if i == len(s) - 1:
            return 1

        res = dp(i + 1)
        if 9 < int(s[i: i + 2]) < 27:
            res += dp(i + 2)

        return res

    return dp(0)
