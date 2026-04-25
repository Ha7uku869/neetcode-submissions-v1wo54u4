class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(lambda : 0)
        for i in range(len(nums)):
            d[nums[i]] += 1
        sorted_items = sorted(d.items(), lambda x:x[1], reversed = True )
        return [x[i] for x in sorted_items[:2]]