class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        ans = []
        min_val = float('inf')
        for c in cost:
            min_val = min(min_val, c)
            ans.append(min_val)
        return ans
