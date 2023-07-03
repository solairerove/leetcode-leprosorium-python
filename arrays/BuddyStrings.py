# O(n) time || O(n) space
def buddy_strings(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    if s == goal and len(set(s)) < len(s):
        return True

    dif = [(a, b) for a, b in zip(s, goal) if a != b]

    return len(dif) == 2 and dif[0] == dif[1][::-1]
