class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = [x*x for x in nums]
        return sorted(ans)
