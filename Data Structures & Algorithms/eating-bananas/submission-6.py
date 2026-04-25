class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        left = 1
        right = max(piles)
        mid = 0
        cleared_k = 0
        while left < right:
            time = 0
            mid = (right - left) // 2 
            for i in range(len(piles)):
                time += math.ceil(piles[i] / k)
            if time <= h:
                cleared_k = k
                right = mid
            else: 
                left = mid


        return k

                    