class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            d[nums[i] % k] = i 
            
            
        return False