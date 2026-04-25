class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right  = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid == tar:
                return mid
            elif mid > tar:
                right = mid
            else:
                left = mid
        return -1

            
