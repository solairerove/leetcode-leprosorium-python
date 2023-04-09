import collections
from typing import List


# O(n + e) time || O(n + e) space
def largest_path_value(self, colors: str, edges: List[List[int]]) -> int:
    adj = {x: [] for x in range(len(colors))}
    for x, y in edges:
        adj[x].append(y)

    visit = [-1] * len(colors)
    max_colors = collections.defaultdict(lambda: [0] * 26)

    def dfs(node):
        if visit[node] == 0:
            return True

        if visit[node] == 1:
            return False

        visit[node] = 0
        mc = [0] * 26
        for neighbor in adj[node]:
            have_cycle = dfs(neighbor)
            if have_cycle:
                return True

            mc = [max(mc[i], max_colors[neighbor][i]) for i in range(len(mc))]
        mc[ord(colors[node]) - ord('a')] += 1
        max_colors[node] = mc

        visit[node] = 1

        return False

    for i in range(len(colors)):
        if dfs(i):
            return -1

    res = 0
    for i in max_colors.keys():
        res = max(res, max(max_colors[i]))

    return res
