class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)

        set2 = set(nums2)

        common_elements = set1.intersection(set2)

        return list(common_elements)
