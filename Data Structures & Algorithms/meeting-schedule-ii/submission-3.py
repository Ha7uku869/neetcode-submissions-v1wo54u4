"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        rooms = []
        for interval in intervals:
            start = interval.start
            end = interval.end
            if not rooms:
                rooms.append(interval)
            else:
                for i in range(len(rooms)):
                    if rooms[i].end <= start:
                        rooms[i] = append
                        break
                rooms.append(interval)
        return len(rooms)
            