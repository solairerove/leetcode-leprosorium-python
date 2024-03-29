import itertools


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
def backspace_compare_stack(self, s: str, t: str) -> bool:
    def trim(to_trim):
        stack = []
        for c in to_trim:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()

        return "".join(stack)

    return trim(s) == trim(t)
