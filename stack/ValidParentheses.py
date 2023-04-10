# O(n) time || O(n) space
def is_valid(self, s: str) -> bool:
    dic = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c not in dic:
            stack.append(c)
            continue

        if not stack or stack[-1] != dic[c]:
            return False

        stack.pop()

    return not stack
