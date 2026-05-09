class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        Sum = 0
        def dfs(i):
            
            while Sum <= target:
                if Sum == target:
                    res.append(path[:])
                    return
                path.append(nums[i + 1])
                dfs(i + 1)