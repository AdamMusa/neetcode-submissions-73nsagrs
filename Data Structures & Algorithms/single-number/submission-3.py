class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
            print(f" this is a bit manupulation : {num ^ res}")
        print(f"Final response  : {res}")
        return res