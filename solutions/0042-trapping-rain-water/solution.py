import numpy as np
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        h = np.array(height)
        left_max = np.maximum.accumulate(h)
        right_max = np.maximum.accumulate(h[::-1])[::-1]
        water_levels = np.minimum(left_max, right_max) - h
        return int(np.sum(water_levels))
