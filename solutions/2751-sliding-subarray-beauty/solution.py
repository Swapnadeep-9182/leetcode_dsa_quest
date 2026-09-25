from typing import List
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        count = [0] * 50 
        
        for i, num in enumerate(nums):
            if num < 0:
                count[num + 50] += 1
                
            if i >= k:
                out_num = nums[i - k]
                if out_num < 0:
                    count[out_num + 50] -= 1
            
            if i >= k - 1:
                prefix_sum = 0
                beauty = 0
                for j in range(50):
                    prefix_sum += count[j]
                    if prefix_sum >= x:
                        beauty = j - 50
                        break
                ans.append(beauty)
                
        return ans
