from typing import List


# O(n) time || O(n) space
def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    color_to_change = image[sr][sc]
    if color_to_change == color:
        return image

    def dfs(r, c):
        if image[r][c] != color_to_change:
            return

        image[r][c] = color

        if r > 0:
            dfs(r - 1, c)

        if r < len(image) - 1:
            dfs(r + 1, c)

        if c > 0:
            dfs(r, c - 1)

        if c < len(image[0]) - 1:
            dfs(r, c + 1)

    dfs(sr, sc)

    return image
