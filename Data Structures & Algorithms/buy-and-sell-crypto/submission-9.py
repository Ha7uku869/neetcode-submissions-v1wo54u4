class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ansGain = 0
        for left in range(len(prices)):
            right = len(prices) - 1
            while left < right:
                ansGain = max(ansGain, prices[right] - prices[left])
                right -= 1
        return  ansGain