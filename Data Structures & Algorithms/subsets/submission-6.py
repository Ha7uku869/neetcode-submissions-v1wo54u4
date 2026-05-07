class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def dfs(i):
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(i)
                path.pop()
                dfs(i)
                if i == len(nums) - 1:
                    res.append(path)
        dfs(0)
        return res