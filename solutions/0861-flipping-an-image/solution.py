import numpy as np
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
       return (np.fliplr(image) ^ 1).tolist()
