class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                if nums[left] > nums[mid]:
                    return nums[mid]
                left = mid + 1
                
            elif nums[mid] < nums[right]:
                if nums[right] > nums[mid]:
                    return nums[mid]
                right = mid - 1
                
            else:
                return nums[left]
