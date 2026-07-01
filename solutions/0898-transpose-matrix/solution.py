import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
     np_matrix = np.array(matrix)
     transposed = np_matrix.T
     return transposed.tolist()   
