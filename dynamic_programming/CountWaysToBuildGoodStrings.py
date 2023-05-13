from collections import Counter


# O(high) time || O(high) space
def count_good_strings(self, low: int, high: int, zero: int, one: int) -> int:
    dp = Counter({0: 1})
    mod = 10 ** 9 + 7
    for i in range(1, high + 1):
        dp[i] = (dp[i - zero] + dp[i - one]) % mod

    return sum(dp[i] for i in range(low, high + 1)) % mod
