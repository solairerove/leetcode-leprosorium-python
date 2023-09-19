from typing import List


# O(n) time || O(n) space
def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    curr_color = image[sr][sc]
    if color == curr_color:
        return image

    row, col = len(image), len(image[0])

    def dfs(r, c):
        if curr_color == image[r][c]:
            image[r][c] = color

            if r >= 1:
                dfs(r - 1, c)

            if r < row - 1:
                dfs(r + 1, c)

            if c >= 1:
                dfs(r, c - 1)

            if c < col - 1:
                dfs(r, c + 1)

    dfs(sr, sc)

    return image
