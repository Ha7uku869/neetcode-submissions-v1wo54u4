def maxSubArray(nums):
    # current_sum: 「今見ている位置で終わる部分配列の最大和」= dp[i]相当
    # max_sum:     「全体の答え（dp配列のmax相当）」
    
    current_sum = nums[0]  # dp[0] = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        # DP遷移: dp[i] = max(nums[i], dp[i-1] + nums[i])
        # 「前の和がマイナスなら捨てて、ここから再スタート」
        current_sum = max(nums[i], current_sum + nums[i])
        
        # 全体のmaxを更新（dp配列のmax()相当）
        max_sum = max(max_sum, current_sum)

    return max_sum
