class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        pairs = sorted(freq.items(), key= lambda z: -z[1])
        return [num for num,_ in pairs[:k]]