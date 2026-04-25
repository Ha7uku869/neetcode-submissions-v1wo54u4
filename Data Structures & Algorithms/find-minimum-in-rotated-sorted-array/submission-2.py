class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > nums[right] and nums[left] < nums[mid]:
                if nums[left] > nums[mid]:
                    return mid
                left = mid + 1
                
            elif nums[mid] < nums[right] and nums[left] > nums[mid]:
                if nums[right] > nums[mid]:
                    return mid
                right = mid - 1
                
            else:
                return left
