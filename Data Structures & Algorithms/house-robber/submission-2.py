class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums[0], nums[1])
        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            maxMoney  = max(nums[i - 2] + nums[i], nums[i - 1])
        return maxMoney
