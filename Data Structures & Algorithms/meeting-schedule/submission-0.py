"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = []
        for i in intervals:
            times.append((i.start, "s"))
            times.append((i.end, "e"))
        times.sort()
        for i in range(1, len(times)):
            if times[i-1][1] == times[i][1]:
                return False
        return True