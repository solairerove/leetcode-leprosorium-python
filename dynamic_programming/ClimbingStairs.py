# O(n) time || O(1) space
def climb_stairs(self, n: int) -> int:
    a, b = 1, 1

    for i in range(n - 1):
        a, b = a + b, a

    return a
