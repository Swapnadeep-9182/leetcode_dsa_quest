import numpy as np

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        matrix = np.array(mat)
        
        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)
        
        special_count = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1
                    
        return special_count
