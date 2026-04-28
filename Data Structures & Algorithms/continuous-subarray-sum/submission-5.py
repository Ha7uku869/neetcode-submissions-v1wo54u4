from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 「ある余りを最初に観測したindex」を覚えておく辞書
        # 初期値 {0: -1} は、0から始まる部分配列が答えになるケース用
        # (例: nums=[3,1] なら prefix=3 で余り0、初期の -1 と距離 0-(-1)=1... 
        #  実際は prefix=4 で余り1だが、もし [3] だけなら距離は 0-(-1)=1 で長さ条件不可)
        remainder_index = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            r = prefix_sum % k

            if r in remainder_index:
                # 同じ余りを以前見ている = 間の部分和が k の倍数
                if i - remainder_index[r] >= 2:
                    return True
                # 長さ1なら True にできないが、ここで辞書を上書きしてはいけない
                # (後から距離が伸びる可能性があるので、最古のindexを保持)
            else:
                remainder_index[r] = i

        return False