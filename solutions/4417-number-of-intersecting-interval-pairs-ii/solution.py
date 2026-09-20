class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        events = []
        
        # Split each interval into start (+1) and end (-1) events
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
            
        events.sort(key=lambda x: (x[0], -x[1]))
        
        total_intersections = 0
        active_intervals = 0
        
        for time, event_type in events:
            if event_type == 1:
                # Every existing active interval intersects with this new one
                total_intersections += active_intervals
                active_intervals += 1
            else:
                active_intervals -= 1
                
        return total_intersections

