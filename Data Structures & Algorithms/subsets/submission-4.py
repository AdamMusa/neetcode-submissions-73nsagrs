class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrakc(i):
            if i == len(nums):
                res.append(path[:])
                return
            path.append(nums[i])
            backtrakc(i + 1)
            path.pop()
            backtrakc( i + 1)
        backtrakc(0)
        return res