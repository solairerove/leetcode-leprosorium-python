from typing import List


# O(n^2) time || O(n) space
def generate_parenthesis_dfs(self, n: int) -> List[str]:
    res = []

    def dfs(left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return

        if left < n:
            dfs(left + 1, right, s + '(')

        if right < left:
            dfs(left, right + 1, s + ')')

    dfs(0, 0, '')

    return res


# O(n^2) time || O(n) space
def generate_parenthesis_bfs(self, n: int) -> List[str]:
    res = []
    left = right = 0
    q = [(left, right, '')]
    while q:
        left, right, s = q.pop()

        if len(s) == n * 2:
            res.append(s)

        if left < n:
            q.append((left + 1, right, s + '('))

        if right < left:
            q.append((left, right + 1, s + ')'))

    return res
