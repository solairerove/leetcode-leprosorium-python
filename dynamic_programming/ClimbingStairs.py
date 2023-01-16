def climb_stairs(self, n: int) -> int:
    if n <= 3:
        return n

    a, b = 2, 3
    for i in range(4, n + 1):
        a, b = b, a + b

    return b


"""
how to understand how many ways for climbing for 0..nth
2 - 1 = 1, 1 ways
2 - 0 = 2,

3 - 1 = 2, 2 - 2 ways
3 - 2 = 1, 1 - 1 ways
3 ways

4 - 5 -> 1 + 1 + 1 + 1, 2 + 1 + 1, 1 + 2 + 1, 1 + 1 + 2, 2 + 2
4 - 1 = 3, - 3 ways
4 - 2 = 2, - 2 ways
2 + 3 = 5

5 - many -> 1 + 1 + 1 + 1 + 1
            2 + 1 + 1 + 1
            1 + 2 + 1 + 1
            1 + 1 + 2 + 1
            1 + 1 + 1 + 2
            2 + 2 + 1
            2 + 1 + 2
            1 + 2 + 2
5 - 1 = 4, 5 ways
5 - 2 = 3, 3 ways
5 + 3 = 8
"""
