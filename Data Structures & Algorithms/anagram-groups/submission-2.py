class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = "".join(sortetd(s))
            res[sortedS] = s
        return res
            