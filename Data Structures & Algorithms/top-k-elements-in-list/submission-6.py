class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        nums_list = []
        ans = []
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        for key, value in count.items():
            # [回数, 数字] のペアにする
            nums_list.append([value, key])
        
        # リストそのものを並び替える（多い順）
        nums_list.sort(reverse=True)
        for i in range(k):
            ans.append(nums_list[i][1])
        return ans


