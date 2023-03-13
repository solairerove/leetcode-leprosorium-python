# O(n) time || O(1) space
def is_palindrome(self, s: str) -> bool:
    low, high = 0, len(s) - 1
    while low <= high:
        while low <= high and not s[low].isalnum():
            low += 1
        while low <= high and not s[high].isalnum():
            high -= 1

        if low <= high and s[low].lower() != s[high].lower():
            return False

        low, high = low + 1, high - 1

    return True
