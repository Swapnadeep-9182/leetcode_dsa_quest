import numpy as np
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        frequencies = nums[0::2]
        values = nums[1::2]
        return (np.repeat(values,frequencies)).tolist()
