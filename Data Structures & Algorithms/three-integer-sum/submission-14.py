class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = nums.sorted()
        s = set()
        ans_seen = set()
        ans = []


        n = len(nums)
        for num in nums:
            if not num in s:
                s.add(nums[i])
        while left < right:
            for i in range(n):
                for j in range(n):
                    if -(i + j) in s:
                        if [nums[i], nums[j], -(i + j)].sorted() in ans_seen:
                            break
                        ans.append([nums[i], nums[j], -(i + j)].sorted())
                        ans_seen.add([nums[i], nums[j], -(i + j)].sorted())
        return ans

                        



            
