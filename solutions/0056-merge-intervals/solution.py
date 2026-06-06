class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x : x[0])
        merged = []
        merged.append(intervals[0])
        for interval in intervals[1:]:
            last_merged_interval = merged[-1]
            if interval[0] <= last_merged_interval[1]:
                last_merged_interval[1] = max(last_merged_interval[1], interval[1])
            else:
                merged.append(interval)
        return merged
