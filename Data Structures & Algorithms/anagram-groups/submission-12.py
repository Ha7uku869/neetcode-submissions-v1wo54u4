class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = defaultdict(list)
        for i in range(len(strs)):
            d[''.join(sorted(strs[i]))].append(strs[i])

        return d.items()