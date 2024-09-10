# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            for i in range(min(a,b), 0, -1):
                if a % i == b % i == 0:
                    return i
            return 1
            return 1
        def helper(head):
            current = head
            nextpt = current.next
            while current and nextpt:
                value = gcd(current.val, nextpt.val)
                current.next = ListNode(value, nextpt)
                current = nextpt
                if current:
                    nextpt = current.next
            
        helper(head)
        return head
