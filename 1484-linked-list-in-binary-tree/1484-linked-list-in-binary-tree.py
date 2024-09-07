# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        current = head
        queue = deque([(root, [current])])
        while queue:
            node, currentList = queue.pop()
            nextList = [ c.next for c in currentList if c.val == node.val]
            if any(True for c in nextList if c is None):
                return True
            current = head
            nextList.append(current)
            if node.left:
                queue.append((node.left, nextList))
            if node.right:
                queue.append((node.right, nextList))
        return False