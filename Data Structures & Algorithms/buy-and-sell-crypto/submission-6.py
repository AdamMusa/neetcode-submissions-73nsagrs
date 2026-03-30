class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[l]:
                l = i
            else:
                profit = prices[i] - prices[l]
                maxP = max(maxP, profit)
        return maxP