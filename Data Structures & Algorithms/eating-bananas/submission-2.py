class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        while True:
            time = 0
            k += 1
            for i in range(len(piles)):
                time += math.ceil(piles[i] / k)
            if time < h:
                return time

                    