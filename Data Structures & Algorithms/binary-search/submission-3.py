class Solution:
    def search(self, nums: List[int], target: int) -> int:

        return ([i for i in range(len(nums)) if nums[i] == target] or [-1])[0]