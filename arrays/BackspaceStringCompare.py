import itertools


# O(n+m) time || O(1) space
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

    return all(x == y for x, y in itertools.zip_longest(trim(s), trim(t)))


# O(n+m) time || O(n+m) space
def backspace_compare_stack(self, s: str, t: str) -> bool:
    def trim(to_trim):
        res = []
        for c in to_trim:
            if c != '#':
                res.append(c)
            elif res:
                res.pop()

        return "".join(res)

    return trim(s) == trim(t)
