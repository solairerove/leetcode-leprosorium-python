from typing import List


# O(n) time || O(n) space
def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    if original_color == color:
        return image

    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and image[r][c] == original_color:
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

    dfs(sr, sc)

    return image
