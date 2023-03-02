# O(n * log(n)) time || O(1) space
def is_anagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
