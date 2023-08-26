# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        node_list = []
        while (current is not None):
            if (current not in node_list):
                node_list.append(current)
                current = current.next
            else:
                return True
        return False