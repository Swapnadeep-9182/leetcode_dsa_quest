from collections import Counter

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base_pairs = 0
        pair_counts = Counter()
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                base_pairs += 1
            else:
                # Store as a sorted tuple to make the pair unordered
                p = (min(nums[i], nums[i+1]), max(nums[i], nums[i+1]))
                pair_counts[p] += 1
                
        # Get the maximum gain from any single replacement pair
        max_gain = max(pair_counts.values()) if pair_counts else 0
        
        return base_pairs + max_gain
