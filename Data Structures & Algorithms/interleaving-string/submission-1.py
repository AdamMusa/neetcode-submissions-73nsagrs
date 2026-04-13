class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dfs(i, j):
            k = i + j
            if k == len(s3):
                return True

            take_s1 = i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j)
            take_s2 = j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1)

            return take_s1 or take_s2
        return dfs(0, 0)