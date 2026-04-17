class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cnt = 1
        nums.sort()
        max_value = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                cnt += 1
            elif (nums[i + 1] - nums[i]) != 0:
                max_value = max(max_value, cnt)
                cnt = 1
        max_value = max(cnt, max_value)
        return max_value
