class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        insertpos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[insertpos -2]:
                nums[insertpos] = nums[i]
                insertpos = insertpos + 1
        return insertpos
