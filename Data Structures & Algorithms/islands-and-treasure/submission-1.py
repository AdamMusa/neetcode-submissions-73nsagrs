from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1, 0),(0,1), (0, -1)]
        inf = 2147483647
        visit = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or visit[r][c]:
                return inf

            if grid[r][c] == 0:
                return 0

            visit[r][c] = True
            res = inf

            for dx, dy in directions:
                res = min(res, 1 + dfs(r+dx, c+dy))
            visit[r][c] = False
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == inf:
                    grid[r][c] = dfs(r,c)
