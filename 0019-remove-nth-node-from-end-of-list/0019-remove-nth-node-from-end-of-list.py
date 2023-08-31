# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lengthofList(self, head):
        length = 0
        while (head is not None):
            length += 1
            head = head.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.lengthofList(head)
        print(length)
        if (length == n):
            return head.next
        tagart = length - n
        current = head
        index = 0
        while (current is not None):
            if (index + 1 == tagart):
                current.next = current.next.next
                break
            current = current.next
            index += 1
        return head