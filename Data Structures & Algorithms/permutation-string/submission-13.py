# permutation_in_string.py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub = {}
        i = 0
        for k in range(len(s1)):
            sub[s1[k]] = sub.get(s1[k], 0) + 1  

        while i < len(s2):
            sub_sub = sub.copy()    

            # 修正1: 残りの文字数が足りるかチェック
            if s2[i] in sub_sub and i + len(s1) <= len(s2):
                match = True  # フラグを用意
                for j in range(len(s1)):
                    # 修正2: キーが存在しなければ即離脱
                    if s2[i + j] not in sub_sub:
                        match = False
                        break  # ← このウィンドウは順列になりえないので抜ける
                    sub_sub[s2[i + j]] -= 1
                if match and all(v == 0 for v in sub_sub.values()):
                    return True
            i += 1
        
        return False