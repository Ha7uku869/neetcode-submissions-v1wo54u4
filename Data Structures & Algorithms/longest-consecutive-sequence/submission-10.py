class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                cnt += 1
            elif nums[i + 1] - nums[i] != 0:
                cnt += 0
        return cnt
