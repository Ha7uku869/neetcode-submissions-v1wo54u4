class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ansGain = 0
        right = len(prices) - 1
        for left in range(len(prices)):
            while left < right:
                ansGain = max(ansGain, prices[right] - prices[left])
                right -= 1
        return  ansGain