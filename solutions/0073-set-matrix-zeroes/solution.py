class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Track the original zeros
        zero_rows = set()
        zero_cols = set()

        # Step 2: First pass to locate all zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Step 3: Second pass to modify the matrix based on our tracked coordinates
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
                    
        return matrix
