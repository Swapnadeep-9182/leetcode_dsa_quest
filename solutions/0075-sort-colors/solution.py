class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1

        def quick_sort(arr,low,high):
            if low < high:
                pivot = partition(nums,low,high)
                quick_sort(nums,low,pivot-1)
                quick_sort(nums,pivot+1,high)

        def partition(arr,low,high):
            p = nums[low]
            i = low + 1
            j = high

            while True:
                while i<=j and nums[i]<=p:
                    i += 1
                while i<=j and nums[j]>=p:
                    j -= 1
                if i<=j:
                    nums[i],nums[j] = nums[j],nums[i]
                else:
                    break
            nums[low],nums[j] = nums[j],nums[low]
            
            return j

        quick_sort(nums, low, high)
