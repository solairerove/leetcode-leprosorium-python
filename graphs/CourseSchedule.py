from typing import List


# O(n + e) time || O(n + e) space
def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
    adj = [[] for i in range(num_courses)]
    degree = [0] * num_courses
    for x, y in prerequisites:
        adj[x].append(y)
        degree[y] += 1

    bfs = [i for i in range(num_courses) if degree[i] == 0]
    for node in bfs:
        for neighbor in adj[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                bfs.append(neighbor)

    return len(bfs) == num_courses
