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
            nums_list.append(key)
        
        sorted(nums_list)
        for i in range(key):
            ans.append(i)
        return ans


