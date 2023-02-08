# O(n) time || O(1) space
def tribonacci(self, n: int) -> int:
    a, b, c = 1, 0, 0
    for _ in range(n):
        a, b, c = b, c, a + b + c

    return c
