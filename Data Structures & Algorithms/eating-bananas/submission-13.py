class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        mid = 0
        while left < right:
            time = 0
            mid = (right + left) // 2 
            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)
            if time <= h:
                right = mid
            else: 
                left = mid + 1


        return right

                    