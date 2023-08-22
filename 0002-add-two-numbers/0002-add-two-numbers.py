# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lengthOfList(self, listNode: Optional[ListNode])->int:
        length = 0
        while (listNode is not None):
            listNode = listNode.next
            length += 1
        return length

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (self.lengthOfList(l2) > self.lengthOfList(l1)):
            l1, l2 = l2, l1
        
        currentList1 = l1
        currentList2 = l2
        while (currentList2 is not None):
            value = currentList1.val + currentList2.val
            currentList1.val = value
            currentList1 = currentList1.next
            currentList2 = currentList2.next
        current = l1
        while current is not None:
            if (current.val >= 10):
                current.val -= 10
                if (current.next is None):
                    current.next = ListNode(1)
                else:
                    current.next.val += 1
            current = current.next
        return l1