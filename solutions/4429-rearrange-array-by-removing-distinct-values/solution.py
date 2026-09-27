from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # 1. Count the frequency of each number
        counts = Counter(nums)
        
        # 2. Get the unique numbers and sort them in ascending order
        sorted_uniques = sorted(counts.keys())
        
        ans = []
        max_freq = max(counts.values()) if nums else 0
        
        # 3. Simulate each round
        for round_idx in range(max_freq):
            for num in sorted_uniques:
                if counts[num] > 0:
                    ans.append(num)
                    counts[num] -= 1
                    
        return ans
        
