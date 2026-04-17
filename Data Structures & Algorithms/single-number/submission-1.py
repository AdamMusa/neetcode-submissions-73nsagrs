class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checker = {}
        res = 0
        for num in nums:
            if num in checker:
                checker[num] = checker.get(num, 0) + 1
            else:
                checker[num] = checker.get(num, 0) + 1
        for num in checker:
            if checker[num] == 1:
                res = num
        return res