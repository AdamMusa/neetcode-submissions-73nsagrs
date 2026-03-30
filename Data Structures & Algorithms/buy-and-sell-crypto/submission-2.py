class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        i = 0
        while i < len(prices):
            maxP = max(maxP, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])
            i+=1
        return maxP