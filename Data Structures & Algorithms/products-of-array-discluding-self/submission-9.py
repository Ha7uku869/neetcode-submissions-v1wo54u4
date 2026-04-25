class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                output[i] *= nums[j]
        return output

                



        
        
        
        