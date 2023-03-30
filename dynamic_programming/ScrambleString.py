# O(n^4) time || O(n^3) space
import collections
from functools import lru_cache


def is_scramble(self, s1: str, s2: str) -> bool:
    @lru_cache(None)
    def dp(s1, s2):
        if s1 == s2:
            return True

        if collections.Counter(s1) != collections.Counter(s2):
            return False

        for i in range(1, len(s1)):
            if dp(s1[:i], s2[:i]) and dp(s1[i:], s2[i:]):
                return True

            if dp(s1[:i], s2[-i:]) and dp(s1[i:], s2[:-i]):
                return True

        return False

    return dp(s1, s2)
