class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prev_s, prev_e = intervals[0]
        for s, e in intervals[1:]:
            if prev_e <= s:
                prev_s, prev_e = s, e
            else:
                res += 1
                prev_e = min(e, prev_e)
        return res
