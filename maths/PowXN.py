# O(x^n) time || O(x^n) space
def my_pow(self, x: float, n: int) -> float:
    if not n:
        return 1

    if n < 0:
        return 1 / my_pow(self, x, -n)

    if n % 2:
        return x * my_pow(self, x, n - 1)

    return my_pow(self, x * x, n // 2)
