class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (len(nums) + 1)
        for i in range(1, n + 1):
            if nums[i - 1] >= nums[i]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i + 1] + 1
        return dp[n + 1] if n >= 1 else 0
                



            