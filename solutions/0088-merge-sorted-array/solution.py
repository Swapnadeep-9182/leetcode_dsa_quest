class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = []
        i,j = 0,0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1

        new.extend(nums1[i:m])
        new.extend(nums2[j:n])
        nums1[:] = new
