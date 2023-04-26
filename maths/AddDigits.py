# O(1) time || O(1) space
def add_digits(self, num: int) -> int:
    return 1 + (num - 1) % 9 if num else 0


# O(n) time || O(n) space
def add_digits_rec(self, num: int) -> int:
    def helper(i):
        if i < 10:
            return i

        res = 0
        for c in str(i):
            res += int(c)

        return helper(res)

    return helper(num)
