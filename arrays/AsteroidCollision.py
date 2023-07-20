from typing import List


# O(n) time || O(n) space
def asteroid_collision(self, asteroids: List[int]) -> List[int]:
    res = []
    for asteroid in asteroids:
        while len(res) and asteroid < 0 < res[-1]:
            if res[-1] == -asteroid:
                res.pop()
                break
            elif res[-1] < -asteroid:
                res.pop()
                continue
            elif res[-1] > -asteroid:
                break
        else:
            res.append(asteroid)

    return res
