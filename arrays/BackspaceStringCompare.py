import itertools
from functools import reduce


# O(n + m) time || O(1) space
def backspace_compare_two_pointers(self, s: str, t: str) -> bool:
    def trim(to_trim):
        skip = 0
        for c in reversed(to_trim):
            if c == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield c

    return all(a == b for a, b in itertools.zip_longest(trim(s), trim(t)))


# O(n + m) time || O(n + m) space
def backspace_compare_stack_2(self, s: str, t: str) -> bool:
    def trim(stack, c):
        if c != '#':
            stack.append(c)
        elif stack:
            stack.pop()

        return stack

    return reduce(trim, s, []) == reduce(trim, t, [])


# O(n + m) time || O(n + m) space
def backspace_compare_stack(self, s: str, t: str) -> bool:
    def trim(line):
        stack = []
        for c in line:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()

        return "".join(stack)

    return trim(s) == trim(t)


# O(n + m) time || O(1) space
def backspace_compare_lambda(self, s: str, t: str) -> bool:
    trim = lambda stack, c: stack[:-1] if c == '#' else stack + c

    return reduce(trim, s, "") == reduce(trim, t, "")


# O(n + m) time || O(1) space
def backspace_compare_two_pointers_straight(self, s: str, t: str) -> bool:
    i, j = len(s) - 1, len(t) - 1
    back_s = back_t = 0
    while True:
        while i >= 0 and (back_s or s[i] == '#'):
            back_s += 1 if s[i] == '#' else -1
            i -= 1

        while j >= 0 and (back_t or t[j] == '#'):
            back_t += 1 if t[j] == '#' else -1
            j -= 1

        if not (i >= 0 and j >= 0 and s[i] == t[j]):
            return i == j == -1

        i, j = i - 1, j - 1
