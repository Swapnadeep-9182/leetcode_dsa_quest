class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_sort(left: int, right: int):
            # Base case: if the segment has 1 or 0 elements, it's already sorted
            if left >= right:
                return
            
            # Find the midpoint to divide the array
            mid = (left + right) // 2
            
            # Recursively sort the left and right halves
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            
            # Merge the two sorted halves together
            merge(left, mid, right)

        def merge(left: int, mid: int, right: int):
            # Temporary list to store the merged sorted elements
            tmp = []
            i, j = left, mid + 1
            
            # Compare elements from both halves and push the smaller one
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            
            # Append any remaining elements from the left half
            while i <= mid:
                tmp.append(nums[i])
                i += 1
                
            # Append any remaining elements from the right half
            while j <= right:
                tmp.append(nums[j])
                j += 1
            
            # Copy the sorted elements from the temporary list back to the original array
            nums[left:right + 1] = tmp

        # Start the merge sort process covering the entire array range
        merge_sort(0, len(nums) - 1)
        return nums

