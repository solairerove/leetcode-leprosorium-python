import collections
from typing import List


# O(n * e) time || O(n + e) space
def find_itinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    itinerary = []

    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        itinerary.append(airport)

    dfs("JFK")

    return itinerary[::-1]
