from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # dp[i] =「インデックスiで終わる部分配列の最大和」
        dp = [0] * n
        dp[0] = nums[0]  # 最初の要素はそれ自身しかない

        for i in range(1, n):
            # 前の結果を延長するか、ここからリセットするか
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        # dp配列全体の中の最大値が答え
        return max(dp)