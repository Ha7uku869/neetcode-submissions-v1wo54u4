class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        sum = 1/2 * n * (n + 1)
        if int(sum) == sum(nums):
            return true
        else:
            return false
        