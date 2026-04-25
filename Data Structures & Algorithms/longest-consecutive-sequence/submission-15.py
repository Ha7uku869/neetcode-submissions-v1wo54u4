class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = 1
        nums.sort()
        max_value = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                cnt += 1
            elif (nums[i + 1] - nums[i]) != 0:
                max_value = max(max_value, cnt)
                cnt = 1
        max_value = max(cnt, maz_value)
        return max_value
