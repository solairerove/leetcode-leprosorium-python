# O(n) time || O(1) space
def is_anagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    arr = [0] * 26
    for ch in s:
        arr[ord(ch) - ord('a')] += 1

    for ch in t:
        arr[ord(ch) - ord('a')] -= 1

    return max(arr) == 0


# O(n * log(n)) time || O(1) space
def is_anagram_naive(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
