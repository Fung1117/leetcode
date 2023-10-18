# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if (len(nums) == 0):
            return None
        max_num = max(nums)
        index = nums.index(max_num)
        head = TreeNode(max_num)
        head.left = self.constructMaximumBinaryTree(nums[:index])
        head.right = self.constructMaximumBinaryTree(nums[index+1:])
        return head 
        