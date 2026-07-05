import numpy as np
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        matrix = np.array([[int(char) for char in row] for row in bank])
        counts = np.sum(matrix,axis=1)
        active_rows = counts[counts > 0]
        if len(active_rows) < 2:
            return 0
        total_beams = np.dot(active_rows[:-1],active_rows[1:])
        return int(total_beams)
