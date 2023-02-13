# O(1) time || O(1) space
def count_odds(self, low: int, high: int) -> int:
    return (high + 1) // 2 - low // 2
