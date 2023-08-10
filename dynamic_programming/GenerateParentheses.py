from typing import List


# O(n^2) time || O(n) space
def generate_parenthesis_top_down(self, n: int) -> List[str]:
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
