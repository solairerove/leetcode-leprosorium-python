from functools import lru_cache
from typing import List


# n^2 recursive traverse of substrings looking for entry in set of words

# O(n^3) time || O(n) space
def word_break_top_down(self, s: str, word_dict: List[str]) -> bool:
    @lru_cache(None)
    def dp(words, i):
        if i == len(s):
            return True

        for j in range(i + 1, len(s) + 1):
            if s[i: j] in words and dp(words, j):
                return True

        return False

    return dp(frozenset(word_dict), 0)


# O(n^2 * m) time || O(1) space
def word_break_constant(self, s: str, word_dict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for w in word_dict:
            if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]


# O(n^3) time || O(n) space
def word_break(self, s: str, word_dict: List[str]) -> bool:
    word_dic = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dic:
                dp[i] = True
                break

    return dp[len(s)]
