class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 答えを入れるリストを全て 1 で初期化しておく
        output = [1] * n

        # ---------------------------------------------------
        # ステップ1：左側からの累積積を計算する
        # ---------------------------------------------------
        left_product = 1
        for i in range(n):
            # 今の場所(i)に、左から持ってきた積を入れる
            output[i] = left_product
            
            # 次の人(i+1)のために、今の数字(nums[i])を掛け算しておく
            left_product *= nums[i]
        
        # この時点で output は「自分より左の積」だけが入った状態
        # 例: [1, 1, 2, 6]
        
        # ---------------------------------------------------
        # ステップ2：右側からの累積積を計算して、合体させる
        # ---------------------------------------------------
        right_product = 1
        # range(開始, 終了, ステップ)
        # n-1 (最後の要素) から 0 まで、-1 ずつ戻るループ
        for i in range(n - 1, -1, -1):
            # すでに入っている「左の積」に、「右の積」を掛ける
            output[i] *= right_product
            
            # 次の人(i-1)のために、今の数字(nums[i])を掛け算しておく
            right_product *= nums[i]
            
        return output