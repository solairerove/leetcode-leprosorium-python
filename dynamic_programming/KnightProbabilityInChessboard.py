import collections


def knight_probability(self, n: int, k: int, row: int, column: int) -> float:
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
