class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                count += 1
        if count != 0:
            count += 1
        return count
            

        