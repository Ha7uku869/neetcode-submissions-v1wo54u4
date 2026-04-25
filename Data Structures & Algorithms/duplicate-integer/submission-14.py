class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i + 1] - nums[i] != 1:
                return True
            else:
                if i == len(nums) - 2:
                    return False