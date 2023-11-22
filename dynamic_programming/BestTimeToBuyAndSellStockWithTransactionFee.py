from typing import List


# O(n) time || O(1) space
def max_profit(self, prices: List[int], fee: int) -> int:
    res, hold = 0, -prices[0]
    for price in prices[1:]:
        res = max(res, hold + price - fee)
        hold = max(hold, res - price)

    return res
