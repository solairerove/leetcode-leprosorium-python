from typing import List


# O(n) time || O(1) space
def max_profit(self, prices: List[int], fee: int) -> int:
    res, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        res = max(res, hold + prices[i] - fee)
        hold = max(hold, res - prices[i])

    return res
