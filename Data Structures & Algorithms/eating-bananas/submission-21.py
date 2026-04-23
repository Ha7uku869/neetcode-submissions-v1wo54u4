class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            midRate = (left + right) // 2
            cnt = sum((pile + midRate - 1) // midRate for pile in piles) 
            if cnt <= h:
                right = midRate - 1
            else:
                left = midRate + 1
        
        return left