import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        min_heap = []  # 各部屋の現在の終了時刻

        for interval in intervals:
            start = interval.start
            end = interval.end

            # 一番早く空く部屋が、この会議の開始時刻までに空いているなら再利用
            if min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)

            # この会議の終了時刻を入れる
            heapq.heappush(min_heap, end)

        return len(min_heap)