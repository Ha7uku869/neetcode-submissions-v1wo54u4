class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()                                    # Line 4
        
        for i, a in enumerate(nums):                   # Line 6
            if i > 0 and a == nums[i - 1]:             # Line 7
                continue                                # Line 8 (重複skip)
            
            l, r = i + 1, len(nums) - 1                 # Line 10 (Two Pointers)
            
            while l < r:                                # Line 11
                threeSum = a + nums[l] + nums[r]        # Line 12
                
                if threeSum > 0:                        # Line 13
                    r -= 1                              # Line 14 (合計大きい→右を小さく)
                    
                elif threeSum < 0:                      # Line 15
                    l += 1                              # Line 16 (合計小さい→左を大きく)
                    
                else:                                   # Line 17 (見つかった！)
                    res.append([a, nums[l], nums[r]])    # Line 18
                    l += 1                              # Line 19
                    while nums[l] == nums[l - 1] and l < r:  # Line 20
                        l += 1                          # Line 21 (重複skip)
        
        return res                                      # Line 22