class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1, max(piles)
        answer = right
        while left <= right:
            m = (left + right)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile)/ m)
            if hours <= h:
                answer = m
                right = m - 1
            else:
                left = m + 1
        return answer 