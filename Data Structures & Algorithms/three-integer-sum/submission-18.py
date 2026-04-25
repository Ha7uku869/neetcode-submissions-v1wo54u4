class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        s = set()
        ans_seen = set()
        ans = []


        n = len(nums)
        for num in nums:
            if not num in s:
                s.add(num)
        for i in range(n):
            for j in range(n):
                if -(i + j) in s:
                    if sorted([nums[i], nums[j], -(i + j)]) in ans_seen:
                        break
                    ans.append(sorted([nums[i], nums[j], -(i + j)]))
                    ans_seen.add(sorted([nums[i], nums[j], -(i + j)]))
        return ans

                        



            
