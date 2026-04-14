class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1) , len(word2)

        def backtrack(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if word1[i] == word2[j]:
                return backtrack(i+1, j+1)
            res = min(backtrack(i+1, j), backtrack(i, j+1))
            res = min(res, backtrack(i+1, j+1))
            return res+1
        return backtrack(0, 0)