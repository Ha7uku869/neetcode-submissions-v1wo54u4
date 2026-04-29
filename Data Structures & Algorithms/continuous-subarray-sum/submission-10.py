class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_mod = prefix_sum % k
            if prefix_mod in d and i - d[prefix_mod] >= 2:
                return True
            elif prefix_mod not in d:
                d[prefix_mod] = i 
            
            
            
        return False