import collections
from functools import reduce
from typing import List


# O(w * n * log(n)) time || O(w * n) space
def group_anagrams(self, strs: List[str]) -> List[List[str]]:
    dic = collections.defaultdict(list)

    for s in strs:
        dic[tuple(sorted(s))].append(s)

    return list(dic.values())


# O(w * n * log(n)) time || O(w * n) space
def group_anagrams_reduce(self, strs: List[str]) -> List[List[str]]:
    return list(reduce(lambda acc, s: acc[tuple(sorted(s))].append(s) or acc, strs, collections.defaultdict(list)).values())


# O(n * m) time || O(n * m) space,
# m - number of strings
# n - average number of letters
def group_anagrams_count_approach(self, strs: List[str]) -> List[List[str]]:
    def get_key(s):
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        return tuple(cnt)

    dic = collections.defaultdict(list)
    for s in strs:
        dic[get_key(s)].append(s)

    return list(dic.values())
