class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelset = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewelset:
                count = count + 1
        return count
