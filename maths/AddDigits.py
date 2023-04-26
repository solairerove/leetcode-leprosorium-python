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
