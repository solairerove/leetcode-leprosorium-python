from typing import List


# O(n) time || O(1) space
def encode(strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s

    return res


# O(n) time || O(1) space
def decode(s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    res, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        offset = j + 1 + length
        res.append(s[j + 1: offset])
        i = offset

    return res
