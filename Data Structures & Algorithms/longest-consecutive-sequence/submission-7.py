class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        start_num = 0
        seen = {}
        for num in nums:
            if num in seen:
                continue
            seen[num] = 1

        for key, val in seen.items():
            if key-1 in seen:
                continue
            else:
                start_num = key-1
        return count

            

        