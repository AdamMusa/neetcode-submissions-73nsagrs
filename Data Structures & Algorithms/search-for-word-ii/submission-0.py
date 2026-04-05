class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        def exist(word)->bool:
            def dfs(r: int, c:int , i:int)->bool:
                if i == len(word):
                    return True
                if r <0 or r >= rows or c < 0 or c >=cols:
                    return False
                
                if board[r][c] != word[i]:
                    return False
                
                char = board[r][c]
                board[r][c] = "#"

                found = (
                    dfs(r +1, c, i +1) or 
                    dfs(r - 1, c, i+1) or 
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1)
                )

                board[r][c] = char
                return found

            for r in range(rows):
                for c in range(cols):
                    if dfs(r,c,0):
                        return True
            return False
        result = []
        for word in words:
            if exist(word):
                result.append(word)
        return result