class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        rigth = len(nums)-1
        
        while left <= rigth:
            middle = (rigth + left ) // 2
            if nums[middle] < target:
                left +=1
            elif nums[middle] > target:
                rigth -=1
            else:
                return middle
        return -1