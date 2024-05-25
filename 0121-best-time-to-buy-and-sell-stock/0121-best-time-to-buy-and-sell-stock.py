class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value = 0
        for i in range(len(prices)-1):
            value = max(value, max(prices[i+1:]) - prices[i])
        return value