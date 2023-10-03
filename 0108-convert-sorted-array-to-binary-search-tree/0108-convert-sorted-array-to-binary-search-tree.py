# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if (len(nums) <= 0):
            return
        n = len(nums)
        tar = n // 2
        val = nums[tar]
        
        return TreeNode(val, self.sortedArrayToBST(nums[:tar]), self.sortedArrayToBST(nums[tar+1:]))