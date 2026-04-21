
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # 「まだ答えが確定していない日」のインデックスを格納
                    # 対応する温度は常に単調減少（stack の下から上にかけて温度が下がる）

        for i, t in enumerate(temperatures):
            # 今日 t が、スタック頂上の日の温度より高ければ、
            # その日にとっての「次に暖かい日」が今日 i だと確定する
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        # ループ終了後、stack に残ったインデックスは「より暖かい日が来なかった」日。
        # ans は 0 で初期化済みなので追加処理は不要。
        return ans