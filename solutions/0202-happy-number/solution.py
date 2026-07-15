class Solution:
    def isHappy(self, n: int) -> bool:
        visited_numbers = set()

        while (n!=1 and n not in visited_numbers):
            visited_numbers.add(n)
            n = self.getSumOfSquares(n)
        
        if (n==1):
            return True
        else:
            return False

    def getSumOfSquares(self, n: int) -> int: 
        total_sum = 0
        while(n>0):
            digit = n%10
            total_sum += (digit*digit)
            n = n//10

        return total_sum
