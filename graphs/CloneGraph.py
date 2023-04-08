import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# O(n + e) time || O(n) space
# n - number of nodes
# e - number of edges
def clone_graph_dfs(self, root: 'Node') -> 'Node':
    visit = {}

    def dfs(node):
        if not node:
            return node

        if node in visit:
            return visit[node]

        clone_node = Node(node.val, [])

        visit[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [dfs(n) for n in node.neighbors]

        return clone_node

    return dfs(root)


# O(n + e) time || O(n) space
# n - number of nodes
# e - number of edges
def clone_graph_bfs(self, root: 'Node') -> 'Node':
    visit = {}
    dq = collections.deque([root])

    def bfs(node):
        if not node:
            return node

        visit[node] = Node(node.val, [])
        while dq:
            n = dq.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visit:
                    visit[neighbor] = Node(neighbor.val, [])
                    dq.append(neighbor)
                visit[n].neighbors.append(visit[neighbor])

        return visit[node]

    return bfs(root)
