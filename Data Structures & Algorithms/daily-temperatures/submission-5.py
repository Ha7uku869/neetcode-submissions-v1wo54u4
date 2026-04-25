class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        for i in range(len(temperatures) - 2):
            for j in range(i + 1, len(temperatures) - 2):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
        ans[len(temperatures) - 1] = 0
        return ans
