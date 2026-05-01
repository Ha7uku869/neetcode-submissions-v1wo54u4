import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        max_heap = []
        for x in stones:
            heapq.heappush(max_heap, -x)
        while len(max_heap) > 1:
            a = heapq.heappop(max_heap)
            b = heapq.heappop(max_heap)
            if a < b:
                heapq.heappush(max_heap, b - a)
            if b < a:
                heapq.heappush(max_heap, a - b)
        return max_heap[0] if max_heap else 0