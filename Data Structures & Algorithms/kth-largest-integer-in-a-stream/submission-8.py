import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        for i in range(self.k - 1):
            heapq.heappop(self.heap)
            
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return heapq.heappop(self.heap)
        
