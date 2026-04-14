class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1) , len(word2)
        memo = {}
        def backtrack(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                res = backtrack(i+1, j+1)
                memo[(i, j)] = res
                return res
            res = min(backtrack(i+1, j), backtrack(i, j+1), backtrack(i+1, j+1))
            memo[(i, j)] = res + 1
            return res + 1
        return backtrack(0, 0)