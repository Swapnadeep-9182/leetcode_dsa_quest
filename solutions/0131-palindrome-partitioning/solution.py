class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        res = []
        is_pal = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
                    
        def backtrack(start, path):
            if start == n:
                res.append(list(path))
                return
            
            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()
                    
        backtrack(0, [])
        return res
