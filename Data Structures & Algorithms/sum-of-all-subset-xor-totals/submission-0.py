class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def dfs(i, xor_val):

            if i == len(nums):
                ans += xor_val
                return

            # nums[i] を選ばない
            dfs(i + 1, xor_val)

            # nums[i] を選ぶ
            dfs(i + 1, xor_val ^ nums[i])

        dfs(0, 0)
        return ans