class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [] * n
        for i in range(len(n)):
            for j in range(i + 1, n - 2):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
        ans[n] = 0
        return ans
