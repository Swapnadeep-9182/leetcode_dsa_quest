class Solution:
    def countOdds(self, low: int, high: int) -> int:
        base_odds = (high-low)//2
        if low%2!=0 or high%2!=0:
            base_odds += 1
        return base_odds
