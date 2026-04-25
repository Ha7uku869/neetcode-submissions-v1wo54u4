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
                    if tuple(sorted([nums[i], nums[j], target])) in ans_seen:
                        break
                    ans.append(tuple(sorted([nums[i], nums[j], target])))
                    ans_seen.add(tuple(sorted([nums[i], nums[j], target])))
        return ans

                        



            
