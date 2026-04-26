# maximum_subarray.py

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current: 「今の要素を末尾とする部分配列の最大和」（dp[i]に相当）
        # result:  「これまで見た中での最大和」
        current = nums[0]
        result  = nums[0]
        # ↑ 全要素が負でも正しく動くよう、0ではなくnums[0]で初期化

        for num in nums[1:]:  # nums[1:]：2番目の要素から最後まで
            # 「前の和に今を加える」vs「今から新しく始める」
            current = max(num, current + num)

            # これまでの最大値を更新
            result = max(result, current)

        return result