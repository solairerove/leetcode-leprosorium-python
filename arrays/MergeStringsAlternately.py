# O(n) time || O(1) space
def merge_alternately(self, word1: str, word2: str) -> str:
    idx1, idx2, res = 0, 0, ""
    while idx1 < len(word1) and idx2 < len(word2):
        if idx1 <= idx2:
            res += word1[idx1]
            idx1 += 1
        else:
            res += word2[idx2]
            idx2 += 1

    if idx1 < len(word1):
        res += word1[idx1:]
    elif idx2 < len(word2):
        res += word2[idx2:]

    return res
