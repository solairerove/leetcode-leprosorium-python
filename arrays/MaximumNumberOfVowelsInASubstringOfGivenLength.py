# O(n) time || O(1) space
def max_vowels(self, s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = cnt = 0
    for i, c in enumerate(s):
        if c in vowels:
            cnt += 1

        if i >= k and s[i - k] in vowels:
            cnt -= 1

        res = max(res, cnt)

    return res
