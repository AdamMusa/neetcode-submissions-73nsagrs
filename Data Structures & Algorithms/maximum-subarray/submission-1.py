class Solution:
    def maxSubArray(self, nums):
        curr = nums[0]
        res = nums[0]

        start = 0
        best_start = 0
        best_end = 0

        for i in range(1, len(nums)):
            # Decide: restart or extend
            if nums[i] > curr + nums[i]:
                curr = nums[i]
                start = i   # restart here
            else:
                curr += nums[i]

            # Update best result
            if curr > res:
                res = curr
                best_start = start
                best_end = i

        return res