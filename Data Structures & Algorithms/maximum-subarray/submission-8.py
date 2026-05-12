class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-INF')
        for i in range(len(nums)):
            cur_sum = nums[i]
            for j in range(i + 1, len(nums)):
                cur_sum += nums[j]
                res = max(res, cur_sum)
            cur_sum = nums[i]
        return res
                