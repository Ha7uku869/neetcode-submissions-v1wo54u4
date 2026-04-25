class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            pd = 1
            for j in range(i+1, len(nums)):
                pd *= nums[j]
            output.append(pd)
        return output
        