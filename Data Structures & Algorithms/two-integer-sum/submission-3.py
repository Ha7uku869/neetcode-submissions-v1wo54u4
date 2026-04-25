class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 2):
            for j in range(1, len(nums) - 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        