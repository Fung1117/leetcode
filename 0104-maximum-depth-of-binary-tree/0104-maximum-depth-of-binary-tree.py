# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        stack = deque([root])
        while stack:
            nextStack = deque()
            while stack:
                node = stack.pop()
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            stack = nextStack
            depth += 1
        return depth

        