class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = int(str(x)[::-1])
        return x == y
