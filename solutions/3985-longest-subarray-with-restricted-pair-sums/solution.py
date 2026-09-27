class Solution:
    def maxSubarray(self, nums: list[int]) -> int:
        freq = [0] * 501
        
        def is_valid(x: int) -> bool:
            # Rule 1: check if two distinct elements in the window sum up to x (v + u = x)
            for v in range(1, (x // 2) + 1):
                u = x - v
                if v == u:
                    if freq[v] >= 2:
                        return False
                else:
                    if freq[v] >= 1 and freq[u] >= 1:
                        return False
            
            # Rule 2: check if x plus an element in the window equals another element (x + v = u)
            for v in range(1, 501 - x):
                if freq[v] >= 1 and freq[x + v] >= 1:
                    return False
                    
            return True

        max_len = 0
        l = 0
        
        for r in range(len(nums)):
            # Shrink the window from the left until adding nums[r] doesn't violate the condition
            while not is_valid(nums[r]):
                freq[nums[l]] -= 1
                l += 1
            
            # Include nums[r] into the window
            freq[nums[r]] += 1
            max_len = max(max_len, r - l + 1)
            
        return max_len
