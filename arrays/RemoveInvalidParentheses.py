from typing import List


# TODO: create search or dfs-bfs topic

# O(n) time || O(n) space
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

    res, stack, visited, found = [], [s], {s}, False
    while stack and not found:
        for curr_str in stack:
            if is_valid(curr_str):
                found = True
                res.append(curr_str)
            elif not found:
                for j in range(len(curr_str)):
                    if curr_str[j] not in ['(', ')']:
                        continue

                    new_str = curr_str[:j] + curr_str[j + 1:]
                    if new_str not in visited:
                        visited.add(new_str)
                        stack.append(new_str)

    return res
