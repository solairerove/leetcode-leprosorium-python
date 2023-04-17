from typing import List


# O(n) time || O(n) space
def max_profit(self, prices: List[int], fee: int) -> int:
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])

    return cash
