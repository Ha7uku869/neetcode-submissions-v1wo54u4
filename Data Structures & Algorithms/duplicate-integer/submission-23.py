class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if i == len(nums) - 1:
                break
            if abs(nums[i + 1] - nums[i]) == 0:
                return True
        return False