import collections
from typing import List


# O(w * n * log(n)) time || O(wn) space
def group_anagrams(self, strs: List[str]) -> List[List[str]]:
    dic = collections.defaultdict(list)
    for s in strs:
        dic[''.join(sorted(s))].append(s)

    return list(dic.values())
