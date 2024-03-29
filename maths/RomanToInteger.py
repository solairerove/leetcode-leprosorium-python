# O(1) time || O(1) space
def roman_to_int(self, s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "Z": 0}
    res = 0
    s = s + "Z"
    for i in range(1, len(s)):
        if roman[s[i]] <= roman[s[i - 1]]:
            res += roman[s[i - 1]]
        else:
            res -= roman[s[i - 1]]

    return res
