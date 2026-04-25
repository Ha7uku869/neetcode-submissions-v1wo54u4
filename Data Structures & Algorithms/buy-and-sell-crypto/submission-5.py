class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ansGain = 0
        left, right = 0, len(prices) - 1
        for cur in range(len(prices)):
            while left < right:
               ansGain = max(ansGain, prices[right] - prices[left])
        return  ansGain