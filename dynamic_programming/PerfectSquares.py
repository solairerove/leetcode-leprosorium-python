import math


# O(n * sqrt(n)) time || O(n) space
def num_squares(self, n: int) -> int:
    square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)

    return int(dp[-1])
