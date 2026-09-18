class Solution:
    def isPalindrome(self, s: str) -> bool:
       ans = "".join(filter(str.isalnum,s)).lower()

       return ans == ans[::-1]
