class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        left = 0
        while left <= len(nums) - 1:
            cur_sum = 0
            cnt = 0
            for right in range(left, len(nums)):
                cur_sum += nums[right]
                cnt += 1
                if cur_sum % k == 0 and nums[right] != 0 and cnt >= 2:
                    return True
            left += 1
        return False        
