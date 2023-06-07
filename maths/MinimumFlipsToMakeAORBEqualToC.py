# O(L) time || O(1) space, L - number of bits
def min_flips(self, a: int, b: int, c: int) -> int:
    return bin(c := (a | b) ^ c).count("1") + bin(a & b & c).count("1")
