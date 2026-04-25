class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_pro = 1
        ans = []
        for num in nums:
            all_pro *= num
        for num in nums:
            ans.append(all_pro // num)

            
