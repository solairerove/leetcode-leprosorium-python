from typing import List


# O(n) time || O(1) space
def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
    if len(flowerbed) == 1:
        return flowerbed[0] == 0 and n <= 1 or flowerbed[0] == 1 and n == 0

    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1

    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1

    for i in range(1, len(flowerbed) - 1):
        if n <= 0:
            break

        if flowerbed[i] == 0:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1

    return n <= 0
