import numpy as np
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matrix = np.array(mat)
        n = len(matrix)
        result = np.trace(matrix) + np.trace(np.fliplr(matrix))
        if n%2 != 0:
            result = result - matrix[n//2][n//2]
        return int(result)
