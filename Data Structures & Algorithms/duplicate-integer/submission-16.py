class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if i == len(nums) - 1:
                break
            if nums[i + 1] - nums[i] != 1:
                return True
        return False