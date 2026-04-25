class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for num in range(nums):
            if num in uniqueSet:
                return True
            else:
                uniqueSet.add(num)
        return False
            