class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else: # nums1 > nums2
                nums1[i], nums2[j] = nums2[j], nums1[i]
                while j + 1 < n and nums2[j] > nums2[j + 1]:
                    nums2[j], nums2[j + 1] = nums2[j + 1], nums2[j]
                    j += 1
                j = 0
        for i in range(n):
            nums1[m + i] = nums2[i]
        
