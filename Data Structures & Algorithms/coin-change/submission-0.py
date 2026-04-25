from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ① dp配列を「到達不能」を意味する大きな値で初期化
        #    amount+1 という値は「絶対に正解にならない枚数」として使う
        dp = [amount + 1] * (amount + 1)

        # ② ベースケース：0円は0枚で作れる
        dp[0] = 0

        # ③ 金額 1 〜 amount を順番に埋める
        for i in range(1, amount + 1):

            # ④ 各コインを試す
            for c in coins:
                if i - c >= 0:
                    # dp[i-c]+1 の意味：
                    # 「残り i-c 円をすでに最適に作れているなら、
                    #   そこにコイン c を1枚足せば i 円になる」
                    dp[i] = min(dp[i], dp[i - c] + 1)

        # ⑤ 結果の取り出し
        # dp[amount] が初期値のままなら作れなかった → -1
        return dp[amount] if dp[amount] != amount + 1 else -1