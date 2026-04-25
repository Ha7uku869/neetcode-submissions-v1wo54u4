class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen = {}
        output = []

        for num in nums:
            pd = 1
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

            for key, value in seen.items():
                if key == num:
                    value -= 1
                    if value == 0:
                        continue
                pd *= key ** value
            output.append(pd)
        return output



        
        
        
        