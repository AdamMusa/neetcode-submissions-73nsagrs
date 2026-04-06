from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        # Step 1: add all treasure cells to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: BFS from all treasures at once
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Skip out of bounds
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Only visit INF land cells
                if grid[nr][nc] != INF:
                    continue

                # Update distance
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))