# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while (current is not None):
            if (current.next is None):
                break
            if (current.val == current.next.val):
                current.next = current.next.next
                continue
            current = current.next
        return head