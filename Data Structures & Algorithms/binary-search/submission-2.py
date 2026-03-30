class Solution:
    def search(self, nums: List[int], target: int) -> int:

        return next((i for i in range(len(nums)) if nums[i] == target), -1)