class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # ✅ max(2,9)=9  ← たまたま今回は同じだが本質的に違う

        for i in range(2, len(nums)):
            dp[i]  = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
