class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def dfs():
            for i in range(len(nums)):
                path.append(nums[i])
                dfs()
                path.pop()
                dfs()
                if i == len(nums):
                    res.append(path)

        return res