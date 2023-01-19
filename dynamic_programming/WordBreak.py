from typing import List


# O(n^3) time || O(n) space
def word_break(self, s: str, word_dict: List[str]) -> bool:
    word_dic = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dic:
                dp[i] = True
                break

    return dp[len(s)]
