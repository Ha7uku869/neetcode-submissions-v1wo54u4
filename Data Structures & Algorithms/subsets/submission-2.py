class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def dfs():
            if len(path) == len(nums):
                res.append(path)
                return
            for i in range(len(nums)):
                path.append(nums[i])
                dfs()
                path.pop()
                dfs()
        return res