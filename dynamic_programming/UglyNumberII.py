# O(n) time || O(n) space
def nth_ugly_number_pre_calculated(self, n: int) -> int:
    ugly = sorted(2 ** a * 3 ** b * 5 ** c
                  for a in range(32) for b in range(20) for c in range(14))

    return ugly[n - 1]
