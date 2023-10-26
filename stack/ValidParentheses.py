# O(n) time || O(n) space
def is_valid(self, s: str) -> bool:
    close_to_open, stack = {")": "(", "]": "[", "}": "{"}, []
    for c in s:
        if c not in close_to_open:
            stack.append(c)
        elif stack:
            if stack.pop() != close_to_open[c]:
                return False
        else:
            return False

    return not stack
