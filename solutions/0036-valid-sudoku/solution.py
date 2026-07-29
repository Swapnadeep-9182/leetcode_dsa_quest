from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):

                current_val = board[r][c]

                if current_val == ".":
                    continue
                
                board_coord = (r//3,c//3)

                if(current_val in rows[r])or(current_val in cols[c])or(current_val in boxes[board_coord]):
                  return False
                
                rows[r].add(current_val)
                cols[c].add(current_val)
                boxes[board_coord].add(current_val)
        
        return True
