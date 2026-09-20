import heapq
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        intersect_count = 0
        active_ends = []
        
        for start, end in intervals:
            while active_ends and active_ends[0] < start:
                heapq.heappop(active_ends)
            intersect_count += len(active_ends)
            heapq.heappush(active_ends, end)
            
        return intersect_count
