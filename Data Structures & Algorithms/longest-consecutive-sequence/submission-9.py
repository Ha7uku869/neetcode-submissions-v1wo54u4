from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 要素数が0の場合は0を返す
        if not nums:
            return 0
            
        # 検索をO(1)で行うためにsetに変換する
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # num-1がセットにない場合、そのnumはシーケンスの開始点である
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 次の数(num+1)が存在する限りカウントを続ける
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # 今回のシーケンス長が過去最大なら更新する
                longest_streak = max(longest_streak, current_streak)

        return longest_streak