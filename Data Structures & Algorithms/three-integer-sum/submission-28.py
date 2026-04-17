# File: three_sum.py

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            # 1つ目の数字が前回と同じ場合はスキップ（組み合わせの重複を防ぐため）
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # 合計が負なら、左ポインタを進めて値を大きくする
                elif total > 0:
                    right -= 1 # 合計が正なら、右ポインタを進めて値を小さくする
                else:
                    # 合計が0になった場合、結果に追加
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # 2つ目、3つ目の数字も、前回と同じ値が連続している場合はスキップ
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # 次の異なる組み合わせを探すため、両方のポインタを動かす
                    left += 1
                    right -= 1
                    
        return ans