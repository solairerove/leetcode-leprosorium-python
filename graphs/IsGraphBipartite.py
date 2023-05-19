from typing import List


# O(n + e) time || O(n + e) space
def is_bipartite(self, graph: List[List[int]]) -> bool:
    color = {}
    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not dfs(self, graph, color, i):
                return False

    return True


def dfs(self, graph, color, pos):
    for i in graph[pos]:
        if i in color:
            if color[i] == color[pos]:
                return False

        else:
            color[i] = 1 - color[pos]
            if not dfs(self, graph, color, i):
                return False

    return True
