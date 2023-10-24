import collections


# O(n) time || O(1) space
def is_anagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    cnt = [0] * 26
    for i in range(len(s)):
        cnt[ord(s[i]) - ord('a')] += 1
        cnt[ord(t[i]) - ord('a')] -= 1

    return max(cnt) == 0


# O(n) time || O(n) space
def is_anagram_counter(self, s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)


# O(n * log(n)) time || O(1) space
def is_anagram_naive(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
