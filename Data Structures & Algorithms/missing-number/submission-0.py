class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = range(n + 1)
        res = 0
        for i in tmp:
            if i in nums:
                continue
            res = i
            break
        return res