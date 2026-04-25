class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = min(piles), max(piles)
        minRate = float('INF')
        while left <= right:
            cnt = 0
            midRate = (left + right) // 2
            for i in range(len(piles)):
                cnt += piles[i] // midRate
                if cnt > h:
                    left = midRate + 1
                    break
            minRate = min(minRate, midRate)
            right = midRate - 1
            
        return minRate