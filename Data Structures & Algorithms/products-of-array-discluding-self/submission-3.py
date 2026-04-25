class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen = {}
        output = []
        pd = 1

        for num in nums:
            seen[num] += 1
            for key, value in seen.items():
                if key == num:
                    value -= 1
                pd *= key ** value
            output.append(pd)
        return output



        
        
        
        