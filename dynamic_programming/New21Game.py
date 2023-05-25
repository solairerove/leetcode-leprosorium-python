# O(n) time || O(n) space
def new_21_game(self, n: int, k: int, max_pts: int) -> float:
    if k == 0 or n >= k + max_pts:
        return 1

    dp = [1.0] + [0.0] * n
    pts_sum = 1.0
    for i in range(1, n + 1):
        dp[i] = pts_sum / max_pts

        if i < k:
            pts_sum += dp[i]

        if i - max_pts >= 0:
            pts_sum -= dp[i - max_pts]

    return sum(dp[k:])
