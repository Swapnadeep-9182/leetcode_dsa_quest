import numpy as np

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        matrix = np.array(mat)
        m, n = matrix.shape
        
        # 1. Create a padded Prefix Sum matrix (zeros on the top and left edge)
        # This padding saves us from annoying "out of bounds" errors during the math
        P = np.zeros((m + 1, n + 1), dtype=int)
        
        # 2. Populate the prefix sums using our cumsum cheat code
        P[1:, 1:] = matrix.cumsum(axis=0).cumsum(axis=1)
        
        # 3. Track the size of our square mansion (k)
        k = 1
        max_size = 0
        
        # We can't build a square bigger than the shortest side of the city
        while k <= min(m, n):
            
            # 4. Calculate the sum of EVERY square of size 'k' at the same time!
            # This is vectorization at its finest.
            square_sums = P[k:, k:] - P[:-k, k:] - P[k:, :-k] + P[:-k, :-k]
            
            # 5. Check if any of those squares are within our budget
            if np.any(square_sums <= threshold):
                max_size = k
                k += 1  # We found one! Let's try to find a bigger one.
            else:
                break   # If we can't afford size k, we definitely can't afford k+1.
                
        return max_size
