from typing import List


# O(n) time || O(1) space
def validate_stack_sequences(self, pushed: List[int], popped: List[int]) -> bool:
    i = j = 0
    for e in pushed:
        pushed[i] = e
        while i >= 0 and pushed[i] == popped[j]:
            i, j = i - 1, j + 1
        i += 1

    return i == 0


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
