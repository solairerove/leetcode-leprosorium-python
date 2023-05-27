from typing import List


# O(n) time || O(1) space
def stone_game_iii(self, stone_value: List[int]) -> str:
    dp = [0] * 3
    for i in range(len(stone_value) - 1, -1, -1):
        dp[i % 3] = max(sum(stone_value[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))

    cmp = lambda a, b: (a > b) - (a < b)

    return ["Tie", "Alice", "Bob"][cmp(dp[0], 0)]
