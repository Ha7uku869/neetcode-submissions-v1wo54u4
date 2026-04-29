"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= prev_end:
                return False
            prev_start, prev_end = start, end            
                        