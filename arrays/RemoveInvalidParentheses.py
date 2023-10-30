import collections
from typing import List


# TODO: create search or dfs-bfs topic

# O(n * 2 ^ n) time || O(2 ^ n) space
def remove_invalid_parentheses(self, s: str) -> List[str]:
    def is_valid(string):
        cnt = 0
        for c in string:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1

            if cnt < 0:
                return False

        return cnt == 0

    res = []
    dq, visited, found = collections.deque([s]), set(), False
    while dq:
        curr_str = dq.popleft()
        if curr_str not in visited:
            visited.add(curr_str)

            if is_valid(curr_str):
                found = True
                res.append(curr_str)

            if not found:
                for i, c in enumerate(curr_str):
                    if c in "()":
                        dq.append(curr_str[:i] + curr_str[i + 1:])

    return res
