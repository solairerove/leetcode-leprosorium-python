# O(n) time || O(n) space
def nth_ugly_number(self, n: int) -> int:
    res = [1]
    prod_2 = prod_3 = prod_5 = 0
    a, b, c = 2, 3, 5
    for i in range(1, n):
        m = min(a, b, c)
        res.append(m)

        if m == a:
            prod_2 += 1
            a = res[prod_2] * 2

        if m == b:
            prod_3 += 1
            b = res[prod_3] * 3

        if m == c:
            prod_5 += 1
            c = res[prod_5] * 5

    return res[-1]


# O(n) time || O(n) space
def nth_ugly_number_pre_calculated(self, n: int) -> int:
    ugly = sorted(2 ** a * 3 ** b * 5 ** c
                  for a in range(32) for b in range(20) for c in range(14))

    return ugly[n - 1]
