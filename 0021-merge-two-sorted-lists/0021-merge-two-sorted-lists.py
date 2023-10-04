# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        if (current1 is None):
            return current2
        if (current2 is None):
            return current1
        if (current1.val > current2.val):
            ans = ListNode(current2.val)
            current2 = current2.next
        else:
            ans = ListNode(current1.val)
            current1 = current1.next

        head = ans
        while (current1 is not None and current2 is not None):
            val1 = current1.val
            val2 = current2.val
            if (val1 > val2):
                tmp = current2
                current2 = current2.next
                tmp.next = None
                ans.next = tmp
                ans = ans.next
            else:
                tmp = current1
                current1 = current1.next
                tmp.next = None
                ans.next = tmp
                ans = ans.next
        if current1 is None:
            ans.next = ListNode(current2.val, current2.next)
        else:
            ans.next = ListNode(current1.val, current1.next)

        return head