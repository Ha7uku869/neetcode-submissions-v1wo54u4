class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right  = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid]== nums[target]:
                return mid
            elif nums[mid] > nums[target]:
                right = mid
            else:
                left = mid
        return -1

            
