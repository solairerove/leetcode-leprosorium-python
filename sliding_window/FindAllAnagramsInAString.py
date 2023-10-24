from typing import List


# O(n) time | O(1) space
def find_anagrams(self, s: str, p: str) -> List[int]:
    s_cnt, p_cnt = [0] * 26, [0] * 26

    for c in s[:len(p)]:
        s_cnt[ord(c) - ord('a')] += 1

    for c in p:
        p_cnt[ord(c) - ord('a')] += 1

    res = []
    if s_cnt == p_cnt:
        res.append(0)

    for i in range(len(p), len(s)):
        s_cnt[ord(s[i]) - ord('a')] += 1
        s_cnt[ord(s[i - len(p)]) - ord('a')] -= 1
        if s_cnt == p_cnt:
            res.append(i - len(p) + 1)

    return res
