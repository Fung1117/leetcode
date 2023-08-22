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
        while (currentList1 is not None):
            
            if (currentList2 is not None):
                value = currentList1.val + currentList2.val
            else:
                value = currentList1.val
            
            if (value >= 10):
                value -= 10
                if (currentList1.next is None):
                    currentList1.next = ListNode(1)
                else:
                    currentList1.next.val += 1
            currentList1.val = value

            currentList1 = currentList1.next
            if (currentList2 is not None):
                currentList2 = currentList2.next
        return l1