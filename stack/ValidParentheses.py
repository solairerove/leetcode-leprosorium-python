# O(n) time || O(n) space
def is_valid(self, s: str) -> bool:
    close_to_open, stack = {")": "(", "]": "[", "}": "{"}, []
    for br in s:
        if br in close_to_open:
            if not stack or close_to_open[br] != stack.pop():
                return False
        else:
            stack.append(br)

    return not stack
