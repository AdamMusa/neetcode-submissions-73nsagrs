class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        pairs = sorted(freq.items(), key= lambda x: -x[1])
        return [num for num, _ in pairs[:k]]
        