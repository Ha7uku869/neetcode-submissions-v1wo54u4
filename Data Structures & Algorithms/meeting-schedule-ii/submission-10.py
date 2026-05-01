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
            print(start, end)
            if not rooms:
                rooms.append(interval)
                print('not rooms')
            else:
                for i in range(len(rooms)):
                    print(i)
                    if rooms[i].end <= start:
                        rooms[i] = interval
                        break
                    rooms.append(interval)
        return len(rooms)
            