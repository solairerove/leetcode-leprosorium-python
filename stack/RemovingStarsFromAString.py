# O(n) time || O(n) space
def remove_stars_stack(self, s: str) -> str:
    stack = []
    for c in s:
        if "*" == c:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)
