class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        for key, value in count.items():
            if key > k:
                break
            else:
                ans.append(key)
        return ans


