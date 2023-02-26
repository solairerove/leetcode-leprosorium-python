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


# O(n * m) time || O(n * m) space
def min_distance_bottom_up(self, word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for i in range(n + 1):
        dp[0][i] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[-1][-1]
