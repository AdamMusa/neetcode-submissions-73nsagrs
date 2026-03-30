class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] in seen:
                return nums[l]
            seen.add(nums[l])
            
            if nums[r] in seen and l != r:
                return nums[r]
            seen.add(nums[r])
            
            l += 1
            r -= 1
        return -1