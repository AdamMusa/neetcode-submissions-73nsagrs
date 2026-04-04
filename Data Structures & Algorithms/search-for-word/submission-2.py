class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, = len(board), len(board[0])
        def backtrack(r, c, i):
           
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if word[i] != board[r][c]:
                return False
            if i == len(word) -1:
                return True
                
            tmp = board[r][c]
            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or 
                backtrack(r, c + 1, i + 1) or 
                backtrack(r, c - 1, i + 1)
            )
            board[r][c]  = tmp
            return found
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False