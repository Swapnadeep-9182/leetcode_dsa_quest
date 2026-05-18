class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_circle = 0
        count_square = 0
        for student in students:
            if student == 0:
                count_circle += 1
            else:
                count_square += 1
        for sandwich in sandwiches:
            if sandwich == 0:
                if count_circle > 0:
                    count_circle -= 1
                else:
                    break
            if sandwich == 1:
                if count_square > 0:
                    count_square -= 1
                else:
                    break
        return count_circle + count_square
