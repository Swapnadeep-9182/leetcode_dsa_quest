from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ans = Counter(nums).most_common(k)
        return [num for num, count in ans]
