class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(nums):
                return 0
            
            lis = dfs(i +1, j)
            if j == -1 or nums[j] < nums[i]:
                lis = max(lis, 1+dfs(i +1, i))
            memo[(i,j)] = lis
            return lis
        sys.setrecursionlimit(2000)
        return dfs(0,-1)