class Solution:
    def findMin(self, nums: List[int]) -> int:
        tmp = []
        mini = nums[0]
        for i in range(len(nums)):
            if nums[i] <= mini:
                mini = nums[i]

        return mini