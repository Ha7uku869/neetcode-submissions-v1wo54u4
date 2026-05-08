class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [False] * len(nums)
        def dfs(i):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
                used[i] == False

        dfs(0)
        return res