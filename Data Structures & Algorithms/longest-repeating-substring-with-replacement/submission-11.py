class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len = 0
        max_count = 0
        left = 0

        for right in range(len(s)):
            # 1. 右端の文字の出現回数をカウント辞書に追加
            count[s[right]] = count.get(s[right], 0) + 1
            
            # 2. 現在のウィンドウ内で「最も多く出現している文字の回数」を更新
            max_count = max(max_count, count[s[right]])

            # 3. ウィンドウ内の文字数から、一番多い文字の数を引く
            # これが「k回以内で変更しなければならない文字数」になります
            # もしこれがkを超えてしまったら、条件を満たさないので左端を1つ縮める
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # 4. 条件を満たしている状態での最大長を記録
            max_len = max(max_len, right - left + 1)

        return max_len