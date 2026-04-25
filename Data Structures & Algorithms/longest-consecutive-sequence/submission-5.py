class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        count = 1
        seen = {}
        for num in nums:
            if num in seen:
                continue
            seen[num] = 1

        return count

            

        