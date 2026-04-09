class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        a, b = 0, 0

        for num in nums:
            a, b = b, max(num + a, b)
        return b