class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans