# O(n) time || O(n) space
def is_valid(self, s: str) -> bool:
    brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for br in s:
        if br in brackets:
            if not stack or stack.pop() != brackets[br]:
                return False
        else:
            stack.append(br)

    return not stack
