import collections
from functools import lru_cache


# O(K*N^2) time || O(K*N^2) space
def knight_probability_top_down(self, n: int, k: int, row: int, column: int) -> float:
    @lru_cache(None)
    def dp(x, y, total):
        if not (0 <= x < n and 0 <= y < n):
            return 0

        if total == 0:
            return 1

        res = 0

        for dx, dy in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]:
            res += dp(x + dx, y + dy, total - 1)

        return res

    return dp(row, column, k) / 8 ** k


# O(8*K*N^2) time || O(N^2) space
def knight_probability_bfs(self, n: int, k: int, row: int, column: int) -> float:
    q = {(row, column): 1}
    level = 0
    dirs = {(dx, dy) for dx in (-2, -1, 1, 2) for dy in (-2, -1, 1, 2) if abs(dx) + abs(dy) == 3}
    in_board = lambda row, column: 0 <= row < n and 0 <= column < n
    while level < k and q:
        nxt = collections.defaultdict(int)
        for coord, cnt in q.items():
            x, y = coord
            for dx, dy in dirs:
                if in_board(x + dx, y + dy):
                    nxt[(x + dx, y + dy)] += cnt

        q = nxt
        level += 1

    return sum(q.values()) / 8 ** k
