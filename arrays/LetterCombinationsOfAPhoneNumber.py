from typing import List


# O(max(n!) time || O(n!) space
def letter_combinations(self, digits: str) -> List[str]:
    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    res = []
    if len(digits) == 0:
        return res

    def dfs(idx, path):
        if idx >= len(digits):
            res.append(path)
            return

        line = dic[digits[idx]]
        for i in line:
            dfs(idx + 1, path + i)

    dfs(0, '')

    return res
