class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len != nums.set():
            return True
        else:
            return False