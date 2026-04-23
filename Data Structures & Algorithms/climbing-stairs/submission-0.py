class Solution:
    def climbStairs(self, n: int) -> int:
        # ベースケース
        if n <= 2:
            return n

        # dp[i] = i段目までの登り方の総数
        dp = [0] * (n + 1)  # インデックス0〜nのリストを用意
        dp[1] = 1  # 1段 → 1通り
        dp[2] = 2  # 2段 → 2通り（1+1 or 2）

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # 漸化式

        return dp[n]