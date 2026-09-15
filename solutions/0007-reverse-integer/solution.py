class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        temp = abs(x)
        ans = 0
        
        while temp > 0:
            a = temp % 10
            temp = temp // 10
            ans = (ans * 10) + a
            
        ans *= sign
        
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
            
        return ans

