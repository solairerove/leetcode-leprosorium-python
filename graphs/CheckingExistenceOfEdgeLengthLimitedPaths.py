from typing import List


# O(n + e) time || O(n + e) space
def distance_limited_paths_exist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
    edges = sorted(edge_list, key=lambda x: x[2])
    res = [False] * len(queries)
    union = UnionFind(n)
    i = 0
    sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][2])
    for q_idx, (u, v, limit) in sorted_queries:
        while i < len(edges) and edges[i][2] < limit:
            union.union_set(edges[i][0], edges[i][1])
            i += 1
        res[q_idx] = union.connected(u, v)

    return res


class UnionFind:
    def __init__(self, size):
        self.parent, self.rank = list(range(size)), [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union_set(self, x, y):
        x_set, y_set = self.find(x), self.find(y)

        if x_set != y_set:
            if self.rank[x_set] < self.rank[y_set]:
                self.parent[x_set] = y_set
            elif self.rank[x_set] > self.rank[y_set]:
                self.parent[y_set] = x_set
            else:
                self.parent[y_set] = x_set
                self.rank[x_set] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
