import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        arr = np.array(grid)
        arr = arr.flatten()
        arr = np.roll(arr,k)
        return arr.reshape(m,n).tolist()
