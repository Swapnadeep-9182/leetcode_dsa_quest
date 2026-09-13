class Solution:
    def firstUniqChar(self, s: str) -> int:
       char_count = {} 

       for char in s:
        char_count[char] = char_count.get(char,0) + 1
       
       for i, c in enumerate(s):
        if char_count[c] == 1:
            return i
       
       return -1
