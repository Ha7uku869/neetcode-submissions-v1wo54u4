class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, cur_total):
            if cur_total == target:
                res.append(path[:])
            if i >= len(nums) or cur_total > target:
                return
            
            path.append(nums[i])
            print("path.append(nums[i]) : " + nums[i])
            dfs(i, cur_total + nums[i])
            path.pop()
            dfs(i + 1, cur_total)

        dfs(0, 0)
        return res