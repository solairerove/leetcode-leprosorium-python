# O(n * m) time || O(n * m) space
def min_distance_naive_recursive(self, word1: str, word2: str) -> int:
    if not word1 and not word2:
        return 0

    if not word1:
        return len(word2)

    if not word2:
        return len(word1)

    if word1[0] == word2[0]:
        return min_distance_naive_recursive(self, word1[1:], word2[1:])

    insert = 1 + min_distance_naive_recursive(self, word1, word2[1:])
    delete = 1 + min_distance_naive_recursive(self, word1[1:], word2)
    replace = 1 + min_distance_naive_recursive(self, word1[1:], word2[1:])

    return min(insert, delete, replace)


# O(n * m) time || O(n * m) space
def min_distance_top_down(self, word1: str, word2: str) -> int:
    def dp(i, j, dic):
        if i == len(word1) and j == len(word2):
            return 0

        if i == len(word1):
            return len(word2) - j

        if j == len(word2):
            return len(word1) - i

        if (i, j) not in dic:
            if word1[i] == word2[j]:
                ans = dp(i + 1, j + 1, dic)
            else:
                insert = 1 + dp(i, j + 1, dic)
                delete = 1 + dp(i + 1, j, dic)
                replace = 1 + dp(i + 1, j + 1, dic)

                ans = min(insert, delete, replace)
            dic[(i, j)] = ans

        return dic[(i, j)]

    return dp(0, 0, {})
