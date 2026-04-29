class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] >= 2:
                return True
        return False