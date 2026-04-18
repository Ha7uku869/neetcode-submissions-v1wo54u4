class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        curMax = 0
        while left < right:
            curMax = max(curMax, min(heights[left], heights[right]) * (right - left))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return curMax
