class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])

        def backtrack(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            found = (
                backtrack(r+1, c)or 
                backtrack(r -1,c) or 
                backtrack(r, c +1) or 
                backtrack(r, c - 1)
            )

            return 1 + found
        area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, backtrack(r,c))
        return area