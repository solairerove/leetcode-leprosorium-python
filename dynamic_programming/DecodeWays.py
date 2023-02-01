# O(n) time || O(1) space
from functools import lru_cache


def num_decodings(self, s: str) -> int:
    if s[0] == "0":
        return 0

    one_back = two_back = 1
    for i in range(1, len(s)):
        curr = 0
        if s[i] != "0":
            curr = one_back

        two_digit = int(s[i - 1: i + 1])
        if 10 <= two_digit <= 26:
            curr += two_back
        two_back, one_back = one_back, curr

    return one_back


# O(n) time || O(n) space
def num_decodings_recursive(self, s: str) -> int:
    @lru_cache(maxsize=None)
    def helper_with_memo(index: int, s: str) -> int:
        if index == len(s):
            return 1

        if s[index] == "0":
            return 0

        if index == len(s) - 1:
            return 1

        ans = helper_with_memo(index + 1, s)
        if int(s[index: index + 2]) <= 26:
            ans += helper_with_memo(index + 2, s)

        return ans

    return helper_with_memo(0, s)
