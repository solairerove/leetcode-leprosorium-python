import collections
from functools import lru_cache
from typing import List


# O(s(w * n)) time || O(n + s) space
def num_ways(self, words: List[str], target: str) -> int:
    n, mod = len(target), 10 ** 9 + 7
    res = [1] + [0] * n
    for i in range(len(words[0])):
        cnt = collections.Counter(w[i] for w in words)
        for j in range(n - 1, -1, -1):
            res[j + 1] += res[j] * cnt[target[j]] % mod

    return res[n] % mod


# O(m * n) time || O(m * n) space
def num_ways_top_down(self, words: List[str], target: str) -> int:
    mod = 10 ** 9 + 7
    m, n = len(words[0]), len(target)
    char_at_index_cnt = [[0] * m for _ in range(128)]
    for word in words:
        for i, c in enumerate(word):
            char_at_index_cnt[ord(c)][i] += 1

    @lru_cache(None)
    def dp(k, i):
        if i == n:
            return 1

        if k == m:
            return 0

        c = target[i]
        res = dp(k + 1, i)
        if char_at_index_cnt[ord(c)][k] > 0:
            res += dp(k + 1, i + 1) * char_at_index_cnt[ord(c)][k]
            res %= mod

        return res

    return dp(0, 0)
