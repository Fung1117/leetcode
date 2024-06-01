# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root, low, high):
            if root is None:
                return 0
            if low <= root.val and root.val <= high:
                return helper(root.left, low, high) + helper(root.right, low, high) + root.val
            # if the current node value < low
            elif low >= root.val:
                return helper(root.right, low, high)
            elif root.val >= high :
                return helper(root.left, low, high)
        return helper(root, low, high)
        