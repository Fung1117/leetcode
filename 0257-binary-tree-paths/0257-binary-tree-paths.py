# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode], s="") -> List[str]:
        if (root is None):
            return []
        if (root.left is None or root.right is None):
            if (root.left is None and root.right is None):
                s += f'{root.val}'
                return [s]
            # elif (root.left is None):

            # elif (root.right is None):

            else:
                s += f'{root.val}->'
        else:
            s += f'{root.val}->'
        return self.binaryTreePaths(root.left, s) + self.binaryTreePaths(root.right, s)