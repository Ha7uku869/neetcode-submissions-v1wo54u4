class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        sum = (n * (n + 1)) // 2
        if sum == int(sum(nums)):
            return true
        else:
            return false
        