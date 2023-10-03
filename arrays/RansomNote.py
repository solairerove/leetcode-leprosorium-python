import collections


# O(n) time || O(n) space
def can_construct(self, ransom_note: str, magazine: str) -> bool:
    if len(ransom_note) > len(magazine):
        return False

    cnt = collections.Counter(magazine)
    for c in ransom_note:
        if c not in cnt or cnt[c] <= 0:
            return False
        cnt[c] -= 1

    return True
