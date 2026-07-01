import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
      rows = len(mat)
      cols = len(mat[0])
      if rows * cols != r*c:
        return mat
      np_mat = np.array(mat)
      reshaped_mat = np.reshape(np_mat,(r,c))
      return reshaped_mat.tolist()
