# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        quque = deque([(root.val, root)])
        while quque:
            sum_of_level = 0
            next_quque = deque()

            while quque:
                sum_of_parent, node = quque.pop()
                sum_of_level += node.val
                next_quque.append((sum_of_parent, node))

            while next_quque:
                sum_of_parent, node = next_quque.pop()
                node.val = sum_of_level - sum_of_parent

                sum_of_parent = 0
                if node.left:
                    sum_of_parent += node.left.val
                if node.right:
                    sum_of_parent += node.right.val

                if node.left:
                    quque.append((sum_of_parent, node.left))
                if node.right:
                    quque.append((sum_of_parent, node.right))
                
        return root
            