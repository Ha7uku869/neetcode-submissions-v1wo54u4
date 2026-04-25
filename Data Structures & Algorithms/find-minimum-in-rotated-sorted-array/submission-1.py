class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] > nums[right] and nums[left] < nums[mid]:
                left = mid + 1
                if nums[left] > nums[mid]:
                    return mid
            elif nums[mid] < nums[right] and nums[left] > nums[mid]:
                right = mid - 1
                if nums[right] > nums[mid]:
                    return mid
            else:
                return left
