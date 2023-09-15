# O(n) time || O(1) space
def is_palindrome(self, s: str) -> bool:
    low, high = 0, len(s) - 1
    while low <= high:
        while low < len(s) - 1 and not s[low].isalnum():
            low += 1

        while high >= 0 and not s[high].isalnum():
            high -= 1

        if s[low].lower() != s[high].lower():
            return False

        low, high = low + 1, high - 1

    return True
