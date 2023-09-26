from typing import List


# O(n) time || O(n) space
def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    color_to_change = image[sr][sc]
    if color == color_to_change:
        return image

    def dfs(r, c):
        if color_to_change == image[r][c]:
            image[r][c] = color

            if r >= 1:
                dfs(r - 1, c)

            if r < len(image) - 1:
                dfs(r + 1, c)

            if c >= 1:
                dfs(r, c - 1)

            if c < len(image[0]) - 1:
                dfs(r, c + 1)

    dfs(sr, sc)

    return image
