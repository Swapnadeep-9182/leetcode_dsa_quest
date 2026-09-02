from bisect import bisect_left, bisect_right
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_index = bisect_left(nums, target)

        if (first_index == len(nums) or nums[first_index] != target):
            return [-1, -1]

        last_index = bisect_right(nums, target) - 1

        return [first_index, last_index]
