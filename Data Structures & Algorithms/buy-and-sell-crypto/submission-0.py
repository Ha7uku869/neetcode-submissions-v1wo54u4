class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=len(prices) - 2
        maxValue = 0
        while i < j:
            if prices[i] > prices[j]:
                i += 1
            else:
                maxValue = max(maxValue, prices[j] - prices[i])
        return 
            