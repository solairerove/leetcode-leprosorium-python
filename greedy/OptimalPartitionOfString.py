# O(n) time || O(1) space
def partition_string(self, s: str) -> int:
    cnt = [0] * 26
    res = 1
    for c in s:
        i = ord(c) - ord('a')
        if cnt[i] == res:
            res += 1
        cnt[i] = res

    return res
