class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = defaultdict(list)
        for i in range(len(strs)):
            d[curstrs[i].sorted()].append()

        return d.items()