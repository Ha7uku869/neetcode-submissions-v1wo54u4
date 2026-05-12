class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, cur_sum):
            if cur_sum == target:
                res.append(path[:])
                return
            if target - (cur_sum + candidates[i]) < 0 or i >= len(candidates):
                return
            path.append(candidates[i])
            dfs(i + 1, cur_sum + candidates[i])
            path.pop()
        
        dfs(0, 0)
        return res
            