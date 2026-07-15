class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        S = sum(nums)
        if(S<=k):
            return 0
        else:
            m = (S-1)//k
        total_cost = (m*(m+1))//2
        return total_cost % MOD
