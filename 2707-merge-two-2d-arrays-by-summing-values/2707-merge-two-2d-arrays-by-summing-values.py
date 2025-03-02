class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        left_pt = 0
        right_pt = 0

        while left_pt < len(nums1) and right_pt < len(nums2):
            if nums1[left_pt][0] == nums2[right_pt][0]:
                ans.append([ nums1[left_pt][0] , nums1[left_pt][1] + nums2[right_pt][1]])
                left_pt += 1
                right_pt += 1
            elif nums1[left_pt][0] < nums2[right_pt][0]:
                ans.append(nums1[left_pt])
                left_pt += 1
            else:
                ans.append(nums2[right_pt])
                right_pt += 1
        if left_pt < len(nums1):
            ans.extend(nums1[left_pt:])
        elif right_pt < len(nums2):
            ans.extend(nums2[right_pt:])

        return ans
