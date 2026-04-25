class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (nums[right] + nums[left]) // 2
            if nums[left] < nums[mid]:
                left = mid + 1
            elif nums[left] > nums[mid]:
                right = mid
        return nums[right]