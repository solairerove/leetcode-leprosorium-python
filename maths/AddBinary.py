# O(n + m) time || O(max(n, m)) space
def add_binary(self, a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    while y:
        x, y = x ^ y, (x & y) << 1

    return bin(x)[2:]


# O(max(n, m)) time || O(max(n, m)) space
def add_binary_naive(self, a: str, b: str) -> str:
    res = ""
    n, m = len(a) - 1, len(b) - 1
    carry = 0
    while n >= 0 or m >= 0:
        total = (int(a[n]) if n >= 0 else 0) + (int(b[m]) if m >= 0 else 0) + carry
        if total <= 1:
            res = str(total) + res
            carry = 0
        else:
            if total % 2 == 0:
                res = "0" + res
            else:
                res = "1" + res
            carry = 1

        n, m = n - 1, m - 1

    if carry == 1:
        res = str(carry) + res

    return res
