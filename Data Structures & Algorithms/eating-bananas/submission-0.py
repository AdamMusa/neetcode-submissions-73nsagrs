class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1, max(piles)
        answer = right
        while left <= right:
            m = (left + right)//2
            hours = sum((p + m -1) // m for p in piles)
            if hours <= h:
                answer = m
                right = m - 1
            else:
                left = m + 1
        return answer 