from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            # nums の最後まで判断し終わったら、今の path を答えに入れる
            if i == len(nums):
                res.append(path[:])
                return

            # 1. nums[i] を入れない場合
            dfs(i + 1)

            # 2. nums[i] を入れる場合
            path.append(nums[i])
            dfs(i + 1)

            # 戻す
            path.pop()

        dfs(0)
        return res