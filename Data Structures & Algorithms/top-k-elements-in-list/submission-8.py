class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(lambda: 0)
        for i in range(len(nums)):
            d[nums[i]] += 1
        d = sorted(d.items(), key=lambda x:x[1], reverse = True)
        return [x[0] for x in sorted_items[:k]]