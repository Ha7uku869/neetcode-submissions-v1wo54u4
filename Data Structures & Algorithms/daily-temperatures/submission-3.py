class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures) - 1):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
        return ans
