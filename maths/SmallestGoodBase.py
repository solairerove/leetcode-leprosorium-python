import math


# O(log(n)) time || O(1) space
def smallest_good_base(self, n: str) -> str:
    n = int(n)
    m_max = int(math.log(n, 2))
    for m in range(m_max, 1, -1):
        k = int(n ** (1 / m))
        if (k ** (m + 1) - 1) == n * (k - 1):
            return str(k)

    return str(n - 1)
