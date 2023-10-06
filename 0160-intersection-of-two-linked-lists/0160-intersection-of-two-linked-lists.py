# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def length(head):
            count = 0
            while (head is not None):
                count += 1
                head = head.next
            return count

        def resizeListedList(head, num):
            for i in range(num):
                head = head.next
            return head

        def isSameListedList(headA, headB):
            while (headA is not None):
                if (headA.val != headB.val):
                    return False
                headA = headA.next
                headB = headB.next
            return True
        lengthA = length(headA)
        lengthB = length(headB)
        if (lengthA > lengthB):
            headA = resizeListedList(headA, lengthA - lengthB)
        else:
            headB = resizeListedList(headB, lengthB - lengthA)
        
        while (headA is not None):
            if (headA == headB):
                return headA
            else:
                headA = headA.next
                headB = headB.next