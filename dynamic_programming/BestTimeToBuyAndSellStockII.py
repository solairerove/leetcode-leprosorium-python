from typing import List


# O(n) time || O(1) space
def max_profit(self, prices: List[int]) -> int:
    res = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            res += prices[i] - prices[i - 1]

    return res
