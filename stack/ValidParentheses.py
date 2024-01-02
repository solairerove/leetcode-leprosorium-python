# O(n) time || O(n) space
def is_valid(self, s: str) -> bool:
    closed_to_open = {'}': '{', ']': '[', ')': '('}
    stack = []
    for br in s:
        if br in closed_to_open:
            if not stack or stack.pop() != closed_to_open[br]:
                return False
        else:
            stack.append(br)

    return not stack
