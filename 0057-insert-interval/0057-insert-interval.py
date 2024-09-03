class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        a1, b1 = newInterval
        minStart, maxEnd = a1, b1
        while index < len(intervals):
            start, end = intervals[index]
            if start <= a1 <= end or start <= b1 <= end or (a1 <= start and b1 >= end):
                minStart = min(start, minStart)
                maxEnd = max(end, maxEnd)
                del intervals[index]
            else:
                index += 1
        intervals.append([minStart, maxEnd])
        intervals.sort()
        return intervals
