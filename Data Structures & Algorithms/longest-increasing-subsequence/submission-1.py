from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # 全要素を「自分1人だけのLIS」で初期化

        for i in range(n):          # i：末尾候補
            for j in range(i):      # j：i より前の全要素を見る
                if nums[j] < nums[i]:           # 狭義単調増加を満たすなら
                    dp[i] = max(dp[i], dp[j] + 1)  # dp[j]に自分を繋げる

        return max(dp)