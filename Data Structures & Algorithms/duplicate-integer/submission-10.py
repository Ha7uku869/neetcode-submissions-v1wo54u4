class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_ = (n * (n + 1)) // 2
        if sum_ == sum(nums):
            return False
        else:
            return True
        