from typing import List


# O(n * e) time || O(n) space
def max_num_edges_to_remove(self, n: int, edges: List[List[int]]) -> int:
    alice, bob = UnionFind(n), UnionFind(n)
    remove = 0
    for t, u, v in edges:
        if t == 3:
            remove += alice.union_set(u, v)
            bob.union_set(u, v)

    for t, u, v in edges:
        if t == 1:
            remove += alice.union_set(u, v)
        else:
            remove += bob.union_set(u, v)

    if alice.components == bob.components == 1:
        return len(edges) - remove

    return -1


class UnionFind:
    def __init__(self, size):
        self.parent, self.rank, self.components = list(range(size + 1)), [1] * (size + 1), size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union_set(self, x, y):
        x_set, y_set = self.find(x), self.find(y)

        if x_set == y_set:
            return 0

        if self.rank[x_set] > self.rank[y_set]:
            self.rank[x_set] += self.rank[y_set]
            self.parent[y_set] = x_set
        else:
            self.rank[y_set] += self.rank[x_set]
            self.parent[x_set] = y_set

        self.components -= 1

        return 1
