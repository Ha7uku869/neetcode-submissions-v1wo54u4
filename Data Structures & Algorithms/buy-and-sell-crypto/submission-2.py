class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        maxValue = 0
        while j < len(prices) - 1:
            if prices[i] > prices[j]:
                i = j
                j += 1
            else:
                maxValue = max(maxValue, prices[j] - prices[i])

        return maxValue
            