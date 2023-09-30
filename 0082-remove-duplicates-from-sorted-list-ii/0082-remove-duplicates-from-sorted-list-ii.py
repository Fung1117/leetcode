# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return head
        while (head.next is not None and head.val == head.next.val):
            val = head.val
            while (head.val == val):
                head = head.next
                if (head is None):
                    return None
        current = head
        while (current.next is not None):
            if (current.next.next is not None and current.next.val ==  current.next.next.val):
                val = current.next.val
                print(val)
                while (current.next is not None and current.next.val == val):
                    current.next = current.next.next
                continue
            current = current.next
        return head