class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        cur = 1
        for i in range(len(nums)):
            ans[i] = cur
            cur *= ans[i]
        cur = 1
        for i in range(0, len(nums), -1):
            ans[i] *= cur
            cur *= ans[i]
        return ans
