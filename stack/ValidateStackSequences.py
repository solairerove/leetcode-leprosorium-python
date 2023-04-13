from typing import List


# O(n) time || O(n) space
def validate_stack_sequences_using_stack(self, pushed: List[int], popped: List[int]) -> bool:
    stack = []
    i = 0
    for e in pushed:
        stack.append(e)
        while stack and stack[-1] == popped[i]:
            i += 1
            stack.pop()

    return not stack
