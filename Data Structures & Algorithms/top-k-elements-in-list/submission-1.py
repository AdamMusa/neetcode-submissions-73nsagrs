class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        pairs = sorted(freq.items(), key= lambda x: x[1], reverse=True)
        return [num for num, _ in pairs[:k]]
        
            